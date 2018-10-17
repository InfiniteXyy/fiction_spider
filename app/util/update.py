import app.util.spider.jianling as jianling
import app.util.spider.xieshen as xieshen
from app.model.connection import my_db
import time

chapters = my_db["chapters"]
books = my_db["books"]


def refresh_data(book_name, book_url, spider):
    print("正在更新", book_name)
    new_articles = []
    chapter_list = spider.get_article_list()
    print("线上文章：", len(chapter_list))
    cur_documents = list(chapters.find({"book_url": book_url}, {"href": True}))
    print("已有文章：", len(cur_documents))
    for index, i in enumerate(chapter_list):
        if len(list(filter(lambda x: x["href"] == i["href"], cur_documents))) == 0:
            i['content'] = spider.get_content(i['href'])
            print("增加到暂存区： {} ".format(i["title"]))
            i['index'] = index + 1  # set article index
            i['book'] = book_name
            i['book_url'] = book_url
            new_articles.append(i)
    if len(new_articles) == 0:
        print("没有更新!")
    else:
        chapters.insert_many(new_articles)
        print("更新完成！共 {} 章".format(len(new_articles)))
        books.update_one({"url": book_url}, {"$set": {"info": new_articles[-1]["title"], "update_time": time.time()}})
    print("chapter amount:", chapters.estimated_document_count())


if __name__ == '__main__':
    refresh_data("剑灵同居日记", "jianling", jianling)
    refresh_data("逆天邪神", "xieshen", xieshen)

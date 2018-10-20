from multiprocessing.pool import Pool

from app.model.connection import my_db
from app.util.spider.spider import Spider
from app.util.spider.shengwu import Shengwu
from app.util.middleware import send_update_message

import time

chapters = my_db["chapters"]
books = my_db["books"]


def refresh(spider: Spider):
    new_articles = []
    chapter_list = spider.get_article_list()
    cur_documents = list(chapters.find({"book_url": spider.book_url}, {"href": True}))
    print("{}: 线上文章 {} - 已有文章 {}".format(spider.book_name, len(chapter_list), len(cur_documents)), end="")

    for index, i in enumerate(chapter_list):
        if len(list(filter(lambda x: x["href"] == i["href"], cur_documents))) == 0:
            i['content'] = spider.get_content(i['href'])
            i['index'] = index + 1  # set article index
            i['book'] = spider.book_name
            i['book_url'] = spider.book_url
            new_articles.append(i)
            chapters.insert_one(i)
            if index == 0:
                print("")
            print("增加", i['title'])

    if len(new_articles) == 0:
        print("   没有更新!")
    else:
        print("更新完成！共 {} 章".format(len(new_articles)))
        books.update_one({"url": spider.book_url},
                         {"$set": {"info": new_articles[-1]["title"], "update_time": time.time()}})


if __name__ == '__main__':
    # GROUP_START = 1
    # GROUP_END = 20
    # pool = Pool()
    # groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    # pool.map(refresh_data(shengwu), groups)
    # pool.close()
    # pool.join()
    refresh(Shengwu())

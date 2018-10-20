from multiprocessing.pool import Pool
from app.util.bot.qq import send_message
from app.model.connection import my_db
from app.util.spider.spider import Spider
from app.util.spider.shengwu import Shengwu
from app.util.spider.jianling import Jianling
from app.util.middleware import send_update_message
import time
import threading

THREAD_NUM = 8
chapters = my_db["chapters"]
books = my_db["books"]
subscribe = my_db["subscribe"]


def divide_chunk(data, chunk_size):
    ans = []
    for item in range(chunk_size):
        temp = [x for x in data if x['index'] % chunk_size == item]
        ans.append(temp)
    return ans


def download_chapter(get_content_method, chapter_list):
    for i in chapter_list:
        i['content'] = get_content_method(i['href'])
        print("增加", i['title'])
        time.sleep(0.5)
        chapters.insert_one(i)


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
        href_list = [x['href'] for x in cur_documents]
        new_article_list = []
        for index, item in enumerate(chapter_list):
            if item['href'] not in href_list:
                item['index'] = index + 1
                item['book'] = spider.book_name
                item['book_url'] = spider.book_url
                new_article_list.append(item)

        chunks = divide_chunk(new_article_list, THREAD_NUM)
        pool = []
        for i in range(THREAD_NUM):
            pool.append(threading.Thread(target=download_chapter, args=(spider.get_content, chunks[i],)))
        for i in pool:
            i.start()
        for i in pool:
            i.join()

        items = list(subscribe.find({"book": spider.book_name}))
        for item in items:
            send_message(item.get("name"), spider.book_name + "已经更新啦!" + "更新了{}".format(len(new_articles)))
        # send_message("kyw7", "haha测试而已,没有更新")
        print("更新完成！共 {} 章".format(len(new_article_list)))
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

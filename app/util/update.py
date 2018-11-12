from app.model import connection
from app.util.spider.spider import Spider
from app.middleware import update_message
import time
import datetime
import threading

THREAD_NUM = 8
chapters = connection.my_db["chapters"]
books = connection.my_db["books"]


def divide_chunk(data, chunk_size):
    ans = []
    for item in range(chunk_size):
        temp = [x for x in data if x['index'] % chunk_size == item]
        ans.append(temp)
    return ans


def download_chapter(get_content_method, chapter_list):
    for i in chapter_list:
        i['content'] = get_content_method(i['href'])
        i['update_time'] = time.time()
        print("增加", i['title'])
        time.sleep(0.5)
        chapters.insert_one(i)


def refresh(spider: Spider, sleep_time: float):
    time.sleep(sleep_time)
    # 从线上爬取文章列表
    chapter_list = spider.get_article_list()
    # 从服务器找到现有的文章列表
    cur_documents = list(chapters.find({"book_url": spider.book_url}, {"href": True}))
    print("{}: 线上文章 {} / 已有文章 {}".format(spider.book_name, len(chapter_list), len(cur_documents)),
          end="" if len(chapter_list) == len(cur_documents) else "\n")
    if len(chapter_list) == len(cur_documents):
        print(" - 没有更新!")
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

        print("更新完成！共 {} 章".format(len(new_article_list)))
        books.update_one({"url": spider.book_url},
                         {"$set": {"info": chapter_list[-1]["title"], "update_time": time.time()}})
        update_message.on_update(spider.book_url, spider.book_name, new_article_list)


if __name__ == '__main__':
    pass

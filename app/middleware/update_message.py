import requests
from urllib import parse
import app.model.subscribe_model as subscribe_model
import time

URL = "http://118.25.8.154/api/send/buddy"


def send_QQ(username, content):
    return requests.get("{}/{}/{}".format(URL, username, content))


def get_subscribe_list(book_url):
    return [x['nickname'] for x in subscribe_model.get_subscribe_list_by_book(book_url)]


def on_update(book_url, book_title, new_chapters):
    return
    # QQ bot gg
    # url = "http://infinitex.cn/{}?sort=desc".format(book_url)
    chapters_list = "\n".join([x['title'] for x in new_chapters])
    content = "你订阅的小说「{}」更新啦！\n{}".format(book_title, chapters_list)
    for user in get_subscribe_list(book_url):
        pass
        # r = send_QQ(user, content)
        # print(r.text)


if __name__ == '__main__':
    on_update("xieshen", "sodfho", [{"title": "sfad"}])

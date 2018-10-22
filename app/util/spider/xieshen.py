import requests
from .spider import Spider
from pyquery import PyQuery as pq


def find(f, seq):
    for item in seq:
        if f(item):
            return item


class Xieshen(Spider):
    book_name = "逆天邪神"
    book_url = "xieshen"

    @classmethod
    def get_article_list(cls):
        output = []
        r = requests.get("http://www.nitianxieshen.com/")
        r.encoding = "utf-8"
        doc = pq(r.text)
        content = doc('#content')
        header = True
        for container in content.children().items():
            if header:
                header = False
                continue
            for li in container.find("li"):
                li_doc = pq(li)
                children = li_doc.children()
                href = children.attr("href")
                output.append({"title": children.text(), "href": href})
        return output

    @classmethod
    def get_content(cls, url):
        r = requests.get(url)
        r.encoding = "utf-8"
        doc = pq(r.text)
        content = doc(".post_entry").text()
        return "\n".join(content.split("\n")[1:])

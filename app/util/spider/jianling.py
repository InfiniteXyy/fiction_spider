import requests
from .spider import Spider
from pyquery import PyQuery as pq


class Jianling(Spider):
    book_name = "剑灵同居日记"
    book_url = "jianling"

    @classmethod
    def get_article_list(cls):
        output = []
        r = requests.get("https://www.23us.so/files/article/html/14/14474/")
        r.encoding = "utf-8"
        doc = pq(r.text)
        table = doc("table")
        for tr in table("tr"):
            td_list = pq(tr)("td")
            for single in td_list:
                temp = pq(single).children()
                output.append({"title": temp.text(), "href": temp.attr("href")})
        return output

    @classmethod
    def get_content(cls, url):
        r = requests.get(url)
        r.encoding = "utf-8"
        doc = pq(r.text)
        content = doc("#contents").text()
        return content.replace("\n\n", "\n")

import requests
from app.util.spider.spider import Spider
from pyquery import PyQuery as pq


class Longzu5(Spider):
    book_name = "龙族5 悼亡者的归来"
    book_url = "longzu5"

    @classmethod
    def get_article_list(cls):
        r = requests.get("http://www.yunxs.com/longzu5/")
        r.encoding = "utf-8"
        doc = pq(r.text)
        result = []
        content = doc(".list_box")
        for item in content.find("li"):
            li = pq(item)
            href = "http://www.yunxs.com/longzu5/" + li.children().attr("href")
            result.append({"href": href, "title": li.text()})

        return result

    @classmethod
    def get_content(cls, url):
        r = requests.get(url)
        r.encoding = "utf-8"
        doc = pq(r.text)
        data = doc(".box_box").text()
        data_list = list(filter(lambda x: x != '', data.split("\n")))[1:-2]
        return "\n".join(data_list)


if __name__ == '__main__':
    # for i in Longzu5.get_article_list():
    #     print(i["href"], i["title"])
    print(Longzu5.get_content("http://www.yunxs.com/longzu5/9414436.html"))

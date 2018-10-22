import requests
from app.util.spider.spider import Spider
from pyquery import PyQuery as pq


class Quanzhi(Spider):
    book_name = "全职法师"
    book_url = "quanzhifashi"

    @classmethod
    def get_article_list(cls):
        output = []
        r = requests.get("https://www.piaotian.com/html/7/7197/index.html")
        r.encoding = "gbk"
        doc = pq(r.text)
        content = doc(".mainbody .centent")
        a_list = content.find("a")
        for i in a_list:
            chapter = pq(i)
            href = "https://www.piaotian.com/html/7/7197/" + chapter.attr("href")
            output.append({"title": chapter.text(), "href": href})
        return output

    @classmethod
    def get_content(cls, url):
        r = requests.get(url)
        r.encoding = "gbk"
        doc = pq(r.text)
        result = []
        is_content = False
        for i in doc.text().split("\n"):
            if not is_content:
                if "上一章" in i:
                    is_content = True
            else:
                if i.strip() == "":
                    continue
                elif "返回书页" in i:
                    break
                else:
                    result.append(i)
        return "\n".join(result)


if __name__ == '__main__':
    # for i in Quanzhi.get_article_list():
    #     print(i["href"], i["title"])
    print(Quanzhi.get_content("https://www.piaotian.com/html/7/7197/4165042.html"))

import requests
from .spider import Spider
from pyquery import PyQuery as pq
from multiprocessing.pool import Pool


class shengwu(Spider):
    book_name = "圣物星辰"
    book_url = "shengwu"

    @classmethod
    def get_article_list(cls):
        output = []
        req = requests.get("http://www.nitianxieshen.com/shengwu/")
        req.encoding = "utf-8"
        doc = pq(req.text)
        # print(doc)
        content = doc('#content')
        print(content)
        for item in content.children().items():
            for li in item.find("li"):
                li_doc = pq(li)
                # print(li_doc)
                children = li_doc.children()
                href = children.attr("href")
                output.append({"title": children.text(), "href": href})
        return output

    @classmethod
    def get_content(cls,url):
        url = "http://www.nitianxieshen.com/shengwu/1151.html"
        r = requests.get(url)
        r.encoding = "utf-8"
        doc = pq(r.text)
        content = doc(".post_entry").text()
        return "\n".join(content.split("\n")[1:])

#GROUP_START = 1
#GROUP_END = 20
# if __name__ == '__main__':
#     pool = Pool()
#     groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
#     pool.map(get_content(cls,"ff"), groups)
#     pool.close()
#     pool.join()


import requests
from pyquery import PyQuery as pq
from app.util.spider.spider import Spider


class Xiuluo(Spider):
    book_name = "网游之修罗传说"
    book_url = "xiuluo"

    @classmethod
    def get_article_list(cls):
        output = []
        r = requests.get("https://www.piaotian.com/html/3/3564/index.html")
        r.encoding = "gbk"
        doc = pq(r.text)
        content = doc(".mainbody .centent")
        a_list = content.find("a")
        for i in a_list:
            chapter = pq(i)
            href = "https://www.piaotian.com/html/3/3564/" + chapter.attr("href")
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


# GROUP_START = 1
# GROUP_END = 20
# if __name__ == '__main__':
#     pool = Pool()
#     groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
#     pool.map(get_content(cls,"ff"), groups)
#     pool.close()
#     pool.join()

if __name__ == '__main__':
    print(Xiuluo.get_content("https://www.piaotian.com/html/3/3564/1791912.html"))

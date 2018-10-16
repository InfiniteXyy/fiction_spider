import requests
from pyquery import PyQuery as pq


def get_article_list():
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


def get_content(url):
    r = requests.get(url)
    r.encoding = "utf-8"
    doc = pq(r.text)
    content = doc("#contents").text()
    return content.replace("\n\n", "\n")


if __name__ == '__main__':
    print(get_article_list())

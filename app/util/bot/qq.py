import urllib.request as req
import urllib.parse as parse

base_url = "http://127.0.0.1:8188/send/buddy/"


def send_message(friends, content):
    friends = parse.quote(friends)
    content = parse.quote(content)
    url = base_url + friends + "/" + content
    req.urlopen(url)
    print(req)


if __name__ == '__main__':
    str1 = "kyw7"
    str2 = "您订阅的逆天邪神更新啦!点击网址即可观看哦~" \
           "fic.infinitex.cn"
    str3 = parse.quote(str2)
    send_message(str1, str3)

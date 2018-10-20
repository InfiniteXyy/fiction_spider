from datetime import datetime
import time
from app import app
from app.util.update import refresh
from app.util.spider.jianling import Jianling
from app.util.spider.xieshen import Xieshen
from app.util.spider.shengwu import Shengwu
import sys

refresh_list = [Jianling(), Xieshen(), Shengwu()]


def switch_command(arg):
    if arg == "run":
        app.run("0.0.0.0", 5000, True)
    elif arg == "refresh":
        print("++++++++++++++++++++++++++")
        print(datetime.fromtimestamp(time.time()).strftime("%m月%d日 %H:%M:%S"))
        for spider in refresh_list:
            refresh(spider)


if __name__ == '__main__':
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        switch_command(arg)
    else:
        print("参数错误")

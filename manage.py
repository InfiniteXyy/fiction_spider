from datetime import datetime
import time
import sys
import io
from app import app
from app.util.update import refresh_data
from app.util.spider.jianling import Jianling
from app.util.spider.xieshen import Xieshen
from app.util.spider.shengwu import shengwu
import sys

refresh_list = [Jianling(), Xieshen(),shengwu()]


def switch_command(type):
    if type == "run":
        app.run("0.0.0.0", 5000, True)
    elif type == "refresh":
        print("++++++++++++++++++++++++++")
        print(datetime.fromtimestamp(time.time()).strftime("%m月%d日 %H:%M:%S"))
        for i in refresh_list:
            refresh_data(i)


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        switch_command(arg)
    else:
        print("参数错误")

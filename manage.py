from app import app
from app.util.update import refresh_data
from app.util.spider.jianling import Jianling
from app.util.spider.xieshen import Xieshen
import sys

refresh_list = [Jianling(), Xieshen()]


def switch_command(type):
    if type == "run":
        app.run("0.0.0.0", 5000, True)
    elif type == "refresh":
        for i in refresh_list:
            refresh_data(i)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        switch_command(arg)
    else:
        print("错误的参数！")

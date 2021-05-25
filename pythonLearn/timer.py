import threading
import time

'''Timer（定时器）是Thread的派生类，用于在指定时间后调用一个方法'''


def hello():
    print('hello,Timer')


if __name__ == '__main__':
    t = threading.Timer(1.0, hello)
    t.start()

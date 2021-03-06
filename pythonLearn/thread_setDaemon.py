from threading import Thread
import time


class MyThread(Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        time.sleep(5)
        print(f'我是子线程:{self.getName()}')


if __name__ == '__main__':
    t1 = MyThread()
    # 设置为守护线程
    t1.setDaemon(True)
    t1.start()

print("我是主线程！")
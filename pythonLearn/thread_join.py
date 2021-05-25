import threading
import time


class MyThread(threading.Thread):
    def __init__(self, id):
        super(MyThread, self).__init__()
        self.id = id

    def run(self):
        time.sleep(3)
        print(self.id)


if __name__ == '__main__':
    t1 = MyThread(999)
    t1.start()
    t1.join()  # 此处增加join调用，实现先执行子线程后执行主线程
    for i in range(5):
        print(i)

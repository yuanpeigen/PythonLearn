from threading import Thread


class SimpleCreator:
    def __init__(self):
        return

    def f(self, tid):
        print(f'线程执行{tid}')

    def createThread(self):
        for i in range(3):
            t = Thread(target=self.f, args=(i,))
            t.start()


class MyThread(Thread):
    def __init__(self, id):
        super(MyThread, self).__init__()  # 重构run函数必须要写
        self.id = id

    def run(self):  # 重写run方法
        print('task', self.id)


if __name__ == '__main__':
    # sc = SimpleCreator()
    # sc.createThread()
    # 调用自定义类
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    t1.start()
    t2.start()


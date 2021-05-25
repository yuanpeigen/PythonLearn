from multiprocessing import Process
import os

'''进程'''


def info(title):
    print(title)
    print('module name:', os.name)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    print('main line')
    p = Process(target=f, args=('bob',))  # 创建进程
    p.start()
    p.join()

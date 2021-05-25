import threading
import time

'''线程锁'''

num = 0


def run(n):
    lock.acquire()  # 获取锁
    global num
    print(f'start:{num}')
    num += 1
    print('end', num)
    lock.release()  # 释放锁


lock = threading.Lock()  # 实例化一个锁对象
for i in range(200):
    t = threading.Thread(target=run, args=(f't-{i}',))
    t.start()
    t.join()

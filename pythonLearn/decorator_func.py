#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 16:24
# @Author  : Czech.Yuan
# @File    : decorator_func.py

"""
装饰器(函数)练习
"""

import time


# 日志装饰函数
def logger(func):
    def wrapper(*args, **kwargs):
        print(f'开始执行：{func.__name__}函数了')
        func(*args, **kwargs)
        print(f'{func.__name__}函数，执行完毕')

    return wrapper


@logger
def add(x, y):
    print(f'{x} + {y} = {x + y}')


# 函数执行时长装饰函数
def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        cost_time = t2 - t1
        print(f'时间花费：{cost_time}秒')

    return wrapper


@timer
def want_sleep(sleep_time):
    time.sleep(sleep_time)


def say_hello(country):
    def wrapper(func):
        def deco(*args, **kwargs):
            if country == 'china':
                print('你好！')
            elif country == 'japan':
                print('八嘎！')
            else:
                return
            func(*args, **kwargs)

        return deco

    return wrapper


@say_hello('japan')
def japan():
    print('哟西哟西')


@say_hello('china')
def china():
    print('中国')


if __name__ == '__main__':
    # add(1, 99)
    # want_sleep(1)
    china()
    japan()

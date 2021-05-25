#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 17:35
# @Author  : Czech.Yuan
# @File    : decorator_class.py
"""
装饰器（类）练习
"""


class Logger(object):
    # 接收被装饰函数
    def __init__(self, func):
        self.func = func

    # 实现装饰逻辑
    def __call__(self, *args, **kwargs):
        print(f'[INFO]:the function {self.func.__name__}() is running...')
        return self.func(*args, **kwargs)


class LoggerLevel(object):
    # 不再接收被装饰函数，而是接收传入参数
    def __init__(self, level='INFO'):
        self.level = level

    # 接收被装饰函数，实现装饰逻辑
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'[{self.level}]:the function {func.__name__}() is running...')
            func(*args, **kwargs)

        return wrapper


@LoggerLevel('ERROR')
def say(something):
    print(f'say {something}!')


if __name__ == '__main__':
    say('Hello')


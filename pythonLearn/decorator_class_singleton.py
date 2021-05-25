#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 16:27
# @Author  : Czech.Yuan
# @File    : decorator_class_singleton.py
"""
装饰类的装饰器
"""

instancs = {}


def singleton(cls):
    def get_instance(*args, **kwargs):
        cls_name = cls.__name__
        print('===== 1 ====')
        if not cls_name in instancs:
            print('===== 2 ====')
            instance = cls(*args, **kwargs)
            instance[cls_name] = instance
            return instance[cls_name]

    return get_instance


@singleton
class User:
    _instance = None

    def __init__(self, name):
        print('===== 3 ====')
        self.name = name


if __name__ == '__main__':
    a = User('HeiHei')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 14:58
# @Author  : Czech.Yuan
# @File    : sanic_start.py

from sanic import Sanic
from sanic.response import text

app = Sanic('My Hello,World app')


@app.get('/')
async def hello_world(request):
    return text('Hello,world.')

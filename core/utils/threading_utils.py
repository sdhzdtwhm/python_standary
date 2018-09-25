#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/09/25
@filename: threading_utils.py
@author: yanghang
Description:
"""
import threading
import datetime


def fun_timer():
    print('hello timer'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    global timer
    #重复构造定时器
    timer = threading.Timer(10, fun_timer)
    timer.start()


if __name__ == '__main__':
    # 定时调度
    timer = threading.Timer(3, fun_timer)
    timer.start()
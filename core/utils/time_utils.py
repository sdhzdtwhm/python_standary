#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/09/25
@filename: time_utils.py
@author: yanghang
Description:
"""
import datetime
import time

print(time.time())
print(type(datetime.datetime.now()))
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print(type(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
print(time.time())


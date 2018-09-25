#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/09/20
@filename: start.py
@author: sdhzdtwhm
Description:
"""
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import core.main

if __name__ == '__main__':
    core.main.start()

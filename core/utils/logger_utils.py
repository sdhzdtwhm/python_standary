#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/09/20
@filename: logger_utils.py
@author: sdhzdtwhm
Description:
    1.日志工具类
"""
import logging
import logging.handlers


class LoggerUtils:

    def loglog(self, log_filename):
        log_level = logging.DEBUG
        formatter = logging.Formatter("%(asctime)s [filename:%(filename)s] [line:%(lineno)2d] [funcName:%(funcName)s]"
                                      "[levelname:%(levelname)s] %(message)s")
        handler = logging.handlers.RotatingFileHandler(log_filename, mode='a', encoding='utf-8', maxBytes=10*1024*1024, backupCount=5)
        handler.setFormatter(formatter)
        logger = logging.getLogger(log_filename)
        logger.addHandler(handler)
        logger.setLevel(log_level)
        console_handle = logging.StreamHandler()
        console_handle.setLevel(log_level)
        console_handle.setFormatter(formatter)
        logger.addHandler(console_handle)
        return logger

    def file_log(self, log_filename):
        log_level = logging.DEBUG
        formatter = logging.Formatter("%(asctime)s [filename:%(filename)s] [line:%(lineno)2d] [funcName:%(funcName)s]"
                                      "[levelname:%(levelname)s] %(message)s")
        handler = logging.handlers.RotatingFileHandler(log_filename, mode='a', encoding='utf-8', maxBytes=10*1024*1024, backupCount=5)
        handler.setFormatter(formatter)
        logger = logging.getLogger(log_filename)
        logger.addHandler(handler)
        logger.setLevel(log_level)
        return logger

    def console_log(self):
        log_level = logging.DEBUG
        formatter = logging.Formatter("%(asctime)s [filename:%(filename)s] [line:%(lineno)2d] [funcName:%(funcName)s]"
                                      "[levelname:%(levelname)s] %(message)s")
        logger = logging.getLogger()
        logger.setLevel(log_level)
        console_handle = logging.StreamHandler()
        console_handle.setLevel(log_level)
        console_handle.setFormatter(formatter)
        logger.addHandler(console_handle)
        return logger

# def log():
#     log_level = logging.DEBUG
#     logger = logging.getLogger()
#     formatter = logging.Formatter("%(asctime)s %(filename)s [line:%(lineno)2d]-%(funcName)s "
#                                   "%(levelname)s %(message)s")
#     file_time_handler = logging.handlers.TimedRotatingFileHandler('../logs/py.log', when='midnight')
#     file_time_handler.setFormatter(formatter)
#     file_time_handler.setLevel(log_level)
#     file_time_handler.suffix = "%Y%m%d.log"
#     logger.addHandler(file_time_handler)
#
#     console_handle = logging.StreamHandler()
#     console_handle.setLevel(log_level)
#     console_handle.setFormatter(formatter)
#     logger.addHandler(console_handle)
#     return logger

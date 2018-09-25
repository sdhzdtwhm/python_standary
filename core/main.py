#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/09/20
@filename: main.py
@author: sdhzdtwhm
Description:
"""
import os
from core.utils.redis_utils import RedisUtils
from core.utils.config_utils import ConfigUtils
from core.utils.mysql_utils import MysqlUtils
from core.utils.logger_utils import LoggerUtils
from core.utils.ftp_utils import FTPUtils
from core.utils.csv_utils import CSV_Utils

const = ConfigUtils('../conf/config.ini')
REDIS_HOST = const.get_value('redis', 'host')
REDIS_PORT = const.get_value('redis', 'port')
REDIS_PASSWORD = const.get_value('redis', 'password')
MYSQL_HOST = const.get_value('mysql', 'host')
MYSQL_PORT = int(const.get_value('mysql', 'port'))
MYSQL_USERNAME = const.get_value('mysql', 'username')
MYSQL_PASSWORD = const.get_value('mysql', 'password')
MYSQL_DATABASE = const.get_value('mysql', 'database')
FTP_HOST = const.get_value('ftp', 'host')
FTP_PORT = int(const.get_value('ftp', 'port'))
FTP_USERNAME = const.get_value('ftp', 'username')
FTP_PASSWORD = const.get_value('ftp', 'password')
FTP_DIR = const.get_value('ftp', 'ftpdir')

def start():
    """程序入口"""
    logger = LoggerUtils().loglog('../logs/test.log')
    #测试redis_utils中的方法
    redis = RedisUtils(REDIS_HOST, REDIS_PORT, REDIS_PASSWORD)
    redis.set_str('hello','11111')
    logger.info(redis.get_str('hello'))
    # a = redis.get_list('runoobkey')
    # for i in a:
    #     print(i.decode())

    #测试mysql_utils类中的方法
    mysql_conn = MysqlUtils(MYSQL_HOST, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_DATABASE)
    sql = "select * from sys_user"
    a = mysql_conn.execute_query(sql)
    logger.info(a)

    #ftp工具类测试
    try:
        ftp = FTPUtils(FTP_HOST, FTP_PORT, FTP_USERNAME, FTP_PASSWORD)
        os.chdir("d:/")
        ftp.upload_file('centos7_init.sh', FTP_DIR)
    except Exception as e:
        logger.info(e)

    #csv工具类使用测试
    csv = CSV_Utils()
    os.chdir("d:/")
    csv.export_sql_result('result.csv', a)
    pass

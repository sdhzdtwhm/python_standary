#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/09/20
@filename: mysql_utils.py
@author: yanghang
Description:
"""
import pymysql


class MysqlUtils:

    def __init__(self, host, username, password, port, database):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.database = database

    def conn(self):
        conn = pymysql.connect( host=self.host, user=self.username, passwd=self.password, port=self.port, db=self.database, charset='utf8')
        return conn

    def conn_close(self):
        conn = self.conn()
        conn.close()

    def execute_query(self,sql):
        if sql is None:
            print("参数不能为空：sql")
        if len(sql) == 0:
            print("参数不能为空：sql")
        try:
            conn = self.conn()
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute(sql)
            data = cursor.fetchall()
            # data = list(data)
            conn.commit()
            cursor.close()  # 关闭游标
            conn.close()  # 释放数据库资源
            return data
        except Exception as e:
            print(e)

    def execute_insert(self, sql):
        if sql is None:
            print("参数不能为空：sql")
        if len(sql) == 0:
            print("参数不能为空：sql")
        try:
            conn = self.conn()
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            status = cursor.execute(sql)
            if status == 1:
                print('insert is Done')
            else:
                print('insert is Failed')
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(e)

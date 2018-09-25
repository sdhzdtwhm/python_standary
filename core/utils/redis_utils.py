#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/09/20
@filename: redis_utils.py
@author: yanghang
Description:
    1.redis 工具类
"""
import redis


class RedisUtils:

    def __init__(self, host, port, password):
        """
        :param host: redis ip
        :param port: redis port
        """
        self.host = host
        self.port = port
        self.password = password

    def single_conn(self):
        pool = redis.ConnectionPool(host=self.host, port=self.port, password = self.password)
        r = redis.Redis(connection_pool=pool)
        return r

    def conn(self):
        #redis单实例连接
        r = self.single_conn()
        #redis cluster连接
        #r = self.cluster_conn()
        return r

    def get_str(self, key):
        r = self.conn()
        result = r.get(key).decode()
        r.connection_pool.disconnect()
        return result

    def set_str(self, key, value):
        r = self.conn()
        r.set(key,value)
        r.connection_pool.disconnect()

    def get_list(self,key):
        r = self.conn()
        result = r.lrange(key, 0, -1)
        r.connection_pool.disconnect()
        return result

    def get_set(self,key):
        r = self.conn()
        pass

    def set_set(self):
        pass

    def get_all_keys(self):
        r = self.conn()
        result = r.keys()
        return result

    def get_all_keys_type(self):
        r = self.conn()
        keys = r.keys()
        for i in keys:
            print(str(i) + '键的类型是' + str(r.type(i)))

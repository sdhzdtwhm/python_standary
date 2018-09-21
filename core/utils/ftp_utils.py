#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/09/20
@filename: ftp_utils.py
@author: yanghang
Description:
    ftp工具类
"""
import ftplib
# from core.utils.logger_utils import LoggerUtils
#
# logger = LoggerUtils().loglog('../logs/ftputils.log')


class FTPUtils:

    def __init__(self, host, port,username, password):
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def ftp_conn(self):
        """
        :return: 返回ftp连接信息
        """
        ftp = ftplib.FTP()
        ftp.connect(self.host, 21)
        ftp.login(self.username, self.password)
        return ftp

    def upload_file(self,filename,file_dir):
        """
        :param filename: 上传文件名称
        :param file_dir: 上传到ftp中的文件夹名称
        :return: 此方法用于向ftp中file_dir文件夹中上传文件
        """
        ftp = self.ftp_conn()
        try:
            ftp.mkd(file_dir)
        except Exception as e:
            e
        ftp.cwd(file_dir)
        ftp.storbinary("STOR " + filename, open(filename, "rb"))
        ftp.quit()

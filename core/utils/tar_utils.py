#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/09/20
@filename: tar_utils.py
@author: yanghang
Description:
"""
import tarfile
import os


class TarUtils:

    def __init__(self, package_dir, package_name, file_path):
        """
        :param package_dir:压缩包存放的文件夹
        :param package_name:压缩包的名称·
        :param file_path:被压缩的文件所在的路径
        """
        self.package_dir = package_dir
        self.package_name = package_name
        self.file_path = file_path

    def tar_dir(self):
        """
            打包函数
        """
        os.chdir(self.package_dir)
        tar = tarfile.open(self.package_name, 'w:gz', encoding='GB2312')
        tar.add(self.file_path)
        tar.close()
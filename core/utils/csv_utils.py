#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/09/21
@filename: csv_utils.py
@author: yanghang
Description:
    1.csv工具类
"""
import csv
import os


class CSV_Utils:

    def csv_reader(self, filename):
        csv_file = open(filename)
        reader_csv =  csv.reader(csv_file)
        csv_data = []
        for row in reader_csv:
            csv_data.append(row)
        csv_file.close()
        return  csv_data

    def csv_writer(self, filename, result):
        csv_file = open(filename, 'a', newline='')
        writer_csv = csv.writer(csv_file)
        writer_csv.writerow(result)
        csv_file.close()

    def export_sql_result(self, filename, result):
        """
        :param filename: 导出文件名称
        :param result: 结果
        :return: 将sql查询结果导入csv中
        """
        with open(filename, 'wb') as f:
            for item in result:
                try:
                    line = ','.join(str(item[key]) for key in item.keys()) + '\n'
                    f.write(line.encode('utf-8'))
                except Exception as e:
                    print(e)
        f.close()


if __name__ == '__main__':
    #测试方法
    info = CSV_Utils()
    a = [{'name': '中信建投证券股份有限公司', 'house_id': '100003'}, {'name': '北京百度网讯科技有限公司(ISP)', 'house_id': '100003'}]
    os.chdir('d:\\')
    info.export_sql_result('3.csv', a)

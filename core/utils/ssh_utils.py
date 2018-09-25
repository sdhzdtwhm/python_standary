#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/09/25
@filename: ssh_utils.py
@author: sdhzdtwhm
Description:
"""
import paramiko


class SSHUtils:

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        try:
            self.transport = paramiko.Transport((self.host, self.port))
            self.transport.connect(username=self.username, password=self.password)
            self.ssh = paramiko.SSHClient()
            self.ssh._transport = self.transport
        except Exception as e:
            print(e)

    def get_result(self, command):
        try:
            stdin, stdout, stderr = self.ssh.exec_command(command)
            result = stdout.readlines()
            for i in range(len(result)):
                print(result[i].strip())
        except Exception as e:
            print(e)

    def close(self):
        try:
            self.transport.close
        except Exception as e:
            print(e)


if __name__ == '__main__':
    ssh = SSHUtils('192.168.2.253',22,'root','Mvtech@123!')
    ssh.get_result('free -m')
    ssh.close()


"""
    # transport = paramiko.Transport(('192.168.2.253',22))
    # transport.connect(username='root', password='Mvtech@123!')
    # ssh = paramiko.SSHClient()
    # ssh._transport = transport
    # stdin,stdout,stderr = ssh.exec_command('df -h')
    # result = stdout.readlines()
    # for i in range(len(result)):
    #     print(result[i].strip())
    # transport.close()
"""

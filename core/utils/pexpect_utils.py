#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018/09/25
@filename: pexpect_utils.py
@author: sdhzdtwhm
Description:
"""
from pexpect import pxssh

host = "192.168.2.253"
username = "root"
password = "Mvtech@123!"
cmd = "uptime"
def sshConnect(host,username,password,cmd):
    try:
        s = pxssh.pxssh()
        s.login(host, username, password)
        s.sendline(cmd)
        s.prompt()
        print(s.before)
        s.logout()
    except:
        print("pxssh failed on login.")

sshConnect(host,username,password,cmd)
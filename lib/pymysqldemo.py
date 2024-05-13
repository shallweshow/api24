#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/18 16:31
# Author : xiaowei
# @File : pymysqldemo.py
# @Software : PyCharm
import pymysql
try:
    # 创建一个连接
    conn=pymysql.connect(host="localhost",port=3306,
                         user="root",password='root',
                         database="p2p",charset="utf8")
    # 创建一个游标
    cursor = conn.cursor()

    # 利用游标对数据库进行操作
    cursor.execute("select * from user")
    # 获取利用游标操作的数据
    data = cursor.fetchone()

    print(data)
except Exception as e:
    print("出错了，错误信息为{}".format(e))

finally:
    # 关闭游标
    if cursor:cursor.close()
    # 关闭连接
    if conn:conn.close()
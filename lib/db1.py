#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/19 8:46
# Author : xiaowei
# @File : db.py
# @Software : PyCharm
import pymysql
import sys
sys.path.append('..')

# 建立数据库的连接
def conn():
    conn =pymysql.connect(
        host="localhost",user="root",
        password="root",db="p2p",
        port=3306,charset="utf8"
    )
    return conn

# 封装数据库的查询操作
def query_db(sql):
    # 建立连接
    con = conn()
    # 建立游标
    cur =con.cursor()
    # 执行sql
    cur.execute(sql)
    # 获取返回的查询结果
    result = cur.fetchall()
    return  result

# 封装数据库的更改操作
def change_db(sql):
    # 建立连接
    con = conn()
    # 建立游标
    cur = con.cursor()
    try:
        # 执行sql
        cur.execute(sql)
        # 提交更改
        con.commit()
    except Exception as e:
        # 回滚
        con.rollback()
    # 获取返回的查询结果
    finally:
        # 关闭游标
        cur.close()
        # 关闭连接
        con.close()
# 封装常用的数据库操作
# 查询
def check_user(num):
    sql="select * from product where pronum = '{}'".format(num)
    result = query_db(sql)
    return  True if result else False
#添加
def add_user(num,name,prolimit,annual):
    sql="insert into product(num,name,prolimit,annualized) values ('{}','{}','{}','{}')".format(num,name,prolimit,annual)
    change_db(sql)
# 删除
def del_user(num):
    sql="delete form product where pronum='{}'".format(num)
    change_db(sql)
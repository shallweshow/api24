#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/15 8:28
# Author : xiaowei
# @File : 接口get请求.py
# @Software : PyCharm
# 导入requests包
import requests,re,hashlib

url="http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"
# 发送了 一个 get请求
r=requests.get(url)
# 获取响应的文本信息
print(r.text)
# 获取当前响应文本，以字节格式展示
# print(r.content)
#
# # 获取当前的url
# print(r.url)
# # 获取当前的状态码
# print(r.status_code)
# # 获取当前的头部信息
# print(r.headers)
# # 获取当前的编码格式
# print(r.encoding)
# # 获取当前的cookies
# print(r.cookies)
#
rw = re.search("id='verifyRand' value='(.+?)'",r.text)
verify = rw.group(1)

print(hashlib.md5(verify.encode()).hexdigest())
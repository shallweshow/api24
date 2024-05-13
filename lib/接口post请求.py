#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/15 8:39
# Author : xiaowei
# @File : 接口post请求.py
# @Software : PyCharm
import  requests

url = 'http://192.168.55.1/zentao/user-login.html'

headers={
"Content-Type": "application/x-www-form-urlencoded"
}
# data={
#     "account":"admin",
#     "password":"5fc0586d0644b685d9bc71ab979cbce5",
#     "verifyRand":"1846341608"
# }
data = "account=admin&password=5fc0586d0644b685d9bc71ab979cbce5&passwordStrength=1&referer=%2Fzentao%2F&verifyRand=1846341608&keepLogin=0"
r = requests.post(url,headers=headers,data=data)
print(r.text)
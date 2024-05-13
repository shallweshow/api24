#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/5/7 16:31
# Author : xiaowei
# @File : 递归.py
# @Software : PyCharm
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

print(sum(5))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
fibonacci(10)


print(fibonacci(10))

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))
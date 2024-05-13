#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/26 9:39
# Author : xiaowei
# @File : send_email_base.py
# @Software : PyCharm
# 连接邮箱
import smtplib
# 发邮件
from email.mime.text import MIMEText
# 发送的对象
msg=MIMEText('不想上班','plain','utf-8')
# 发件人
msg['From']='252553516@qq.com'
# 收件人
msg['To']='252553516@qq.com'
# 邮件主题
msg['Subject']='今天周末' # 邮件主题
# 创建一个smtp的链接
smtp = smtplib.SMTP_SSL('smtp.qq.com')
# 登录发件箱
smtp.login('252553516@qq.com','txekllcllwihbgbh')
# 发送邮件
smtp.sendmail('252553516@qq.com','252553516@qq.com',msg.as_string())
# 退出 断开
smtp.quit()
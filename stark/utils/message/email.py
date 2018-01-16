#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from .base import BaseMessage

class Email(BaseMessage):
    def __init__(self):
        self.email = "ctztiga@163.com"
        self.user = "陈太章"
        #self.pwd = 'zglmzcyjsvppbhic' #qq使用授权码  4927
        self.pwd='492745473CTZ' #163 授权码
        #self.pwd='CTZ492745473'

    def send(self,subject,body,to,name):
        msg = MIMEText(body, 'plain', 'utf-8')  # 发送内容
        msg['From'] = formataddr([self.user,self.email])  # 发件人
        msg['To'] = formataddr([name, to])  # 收件人
        msg['Subject'] = subject # 主题


        server = smtplib.SMTP("smtp.163.com",25) # SMTP服务
        # server = smtplib.SMTP_SSL("smtp.qq.com",465) # SMTP服务 QQ
        server.login(self.email, self.pwd) # 邮箱用户名和密码
        server.sendmail(self.email, [to, ], msg.as_string()) # 发送者和接收者
        server.quit()

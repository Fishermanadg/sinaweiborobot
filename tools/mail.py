#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import smtplib
import config
from email.mime.text import MIMEText
from email.header import Header


def send_mail(errors):
    sender = config.user_email
    receiver = config.user_email
    subject = '微博机器人出错，暂停工作'
    smtpserver = 'smtp.qq.com'
    username = config.user_email
    password = config.user_email_password
    msg = MIMEText(errors, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

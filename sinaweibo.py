#!/usr/bin  /env python
# --*-- coding:utf-8 --*--

__version__ = '1.0.0'
__author__ = 'fishermanadg(fishermanadg@gmail.com)'

'''
python weibo robot for sina
'''

import random
import time
from tools import (send_normal_weibo,
                   send_maidou_weibo,
                   send_weather_weibo)
from tools import weibo_login
from tools import weibo_reply
from tools import send_mail
from tools import (update_localtion_date,
                   call_log)


# check new weibo and comments every minute
def run():
    inter = 60
    client = weibo_login()
    print ('Start Work on %s!\n' % time.asctime())
    try:
        while 1:
            now_hour = time.strftime("%H")
            now_minute = time.strftime("%M")
            now_second = time.strftime("%S")
            now = str(now_hour) + str(now_minute) + str(now_second)
            if now == '000000':
                break
            inter += 1
            if inter > 60:
                weibo_reply(client)
                inter = 0
            if now == '174900':
                send_weather_weibo(client)
            elif (now == '144420' or now == '120000' or now == '090000'):
                send_normal_weibo(client)
            elif (now == '144330'):
                send_maidou_weibo(client)
            elif (now_second == second and
                  now_minute == minute and
                  now_hour == hour):
                send_normal_weibo(client)
            else:
                time.sleep(1)
    except Exception as e:
        print ('Run error: ' + str(e))
        e = 'Time: ' + str(time.asctime()) + ' Error: ' + str(e) + '\n'
        call_log(e, '1')


if (__name__ == '__main__'):
    run_times = 0
    error_times = 0
    while 1:
        hour = random.choice(range(24))
        minute = random.choice(range(60))
        second = random.choice(range(60))
        print ('Random Weibo time：%s:%s:%s' % (hour, minute, second))
        print ('Now time is: %s' % time.asctime())

        if run_times < 3:
            run()
            run_times += 1
        else:
            error_times += 1
            print ("Have lots of Errors, take a rest~")
            t = 10 + error_times * error_times
            time.sleep(t)
            run_times = 0
            if error_times > 5:
                with open('./res/errors.log', 'r') as f:
                    a = str(f.readlines()[-20:])
                try:
                    send_mail(a)
                    print('Errors log has been sent to the specified mailbox.')
                    break
                except e:
                    print('Send mail error! Errors: %s.' % str(e))
                    break

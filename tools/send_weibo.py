#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import random
import time
from get_weather import get_weather
from get_image import *
from tools import *


def send_normal_weibo(client=None):
    # send a normal weibo with a picture.
    if client == None:
        print ('Please login in!')
    else:
        # build image to update
        get_img()
        try:
            with open('./img/temp_image.jpg', 'rb') as img:
                status = 'Share for you~'
                client.statuses.upload.post(status=status, pic=img)
                print ('\nSend a normal weibo success!\n')
        except:
            print ('Send a normal weibo error!')
        else:
            # logging
            tim = time.asctime()
            P = 'Send a normal weibo.  Time：%s.   Content: %s\n\n\n' % (
            tim, status)
            call_log(P)
    return None


def send_maidou_weibo(client=None):
    # send a weibo about maidou.
    if client == None:
        print ('Please login in!')
    else:
        try:
            with open('./res/maidou.txt', 'r') as f:
                mai = f.readlines()
            status = mai[random.randint(0,len(mai)-1)]
            status = status.decode('gb2312').encode('utf-8')
            client.statuses.update.post(status=status)
            print ('\nSend a weibo about maidou success!\n')
        except:
            print ('Send a maidou weibo error!')
        # logging
        tim = time.asctime()
        P = 'Send a weibo about maidou.  Time：%s.   Content: %s\n\n\n' % (
            tim, status)
        call_log(P)
    return None


def send_weather_weibo(client=None):
    # send a weibo about weather.
    if client == None:
        print ('Please login in!')
    else:
        # build bing image to update
        get_bing_img()

        weather_info = get_weather()
        city = weather_info['currentCity'].encode('utf-8')
        date = weather_info['weather_data'][0]['date'].encode('utf-8')
        ti = time.strftime("%Y年%m月%d日 %H时%M分")
        weather = weather_info['weather_data'][0]['weather'].encode('utf-8')
        temp = weather_info['weather_data'][0]['temperature'].encode('utf-8')
        wind = weather_info['weather_data'][0]['wind'].encode('utf-8')
        status = '这里是%s,今天%s,现在是%s,今天天气为%s,温度为%s,%s~' % (
            city, date, ti, weather, temp, wind)
        try:
            with open('./img/Bing_img.jpg', 'rb') as img:
                client.statuses.upload.post(status=status, pic=img)
                print ('\nSend a weibo about weather success!\n')
        except:
            print ('Send a weather weibo error!')
        # logging
        tim = time.asctime()
        P = 'Send a weibo about weather.  Time：%s.   Content: %s\n\n\n' % (
            tim, status)
        call_log(P)
    return None

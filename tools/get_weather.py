#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import re
import requests
import json
import urllib


# get ip address
def get_ip_addr():
    url = 'http://iframe.ip138.com/ic.asp'
    x = requests.get(url).content
    ip_addr = re.search(r'\d+\.\d+\.\d+\.\d+', x).group(0)
    return ip_addr


# get weather information from baidu api
def for_get_weather(c_name):
    if (c_name == ''):
        print ('No city given!')
    else:
        weather_info = requests.get(
            'http://api.map.baidu.com/telematics/v3/weather?location=%s&\
            output=json&ak=2469115471df134bf866a5dc5451e561' % c_name)
        weather_info = json.loads(weather_info.content)
        weather_day = weather_info['results'][0]
    # return weather_day is a dict,include 'currentCity','weather_data'
    return weather_day


# get weather can be call,back dict(unicode coding)
def get_weather(city=None, capital=None):
    if (city == None and capital == None):
        ip = get_ip_addr()
        # get localtion information turn json format from taobao ip library
        location_info = requests.get(
            'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip)
        location_info = json.loads(location_info.content)
        city_name = location_info['data']['city'].encode('utf-8')
        city_name = urllib.quote(city_name)
        c_name = city_name
        weather_day = for_get_weather(c_name)
        return weather_day
    else:
        weather_info = ''
        weather_day = ''
        try:
            city_name = urllib.quote(city)
            capital_name = urllib.quote(capital)
        except:
            city_name = city
            capital_name = capital
        # try getweather information from city_name
        try:
            c_name = city_name
            weather_day = for_get_weather(c_name)['weather_data']
            weather_day.append(0)
        # try get weather information from capital_name
        except:
            try:
                c_name = capital_name
                weather_day = for_get_weather(c_name)['weather_data']
                weather_day.append(1)
            except:
                pass
        if weather_day != '':
            return weather_day
        # if can't get weather_info else back beijing weather_info
        else:
            c_name = urllib.quote('北京')
            weather_day = for_get_weather(c_name)['weather_data']
            weather_day.append(2)
            return weather_day

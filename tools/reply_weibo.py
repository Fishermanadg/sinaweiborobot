#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import requests
import json
import time
from get_weather import get_weather
from tools import call_log, update_localtion_date


def reply_weibo(client,
                last_cwi,
                last_callme_weibo_content):
    if (client == None
            or last_cwi == None
            or last_callme_weibo_content == None):
        print ("Reply weibo error,please check login and weibo id.")
    else:
        # get @me user name, created on and time
        callme_user_info = client.statuses.show.get(id=last_cwi)
        name = callme_user_info['user']['name'].encode('utf-8')
        created_at = callme_user_info['created_at'].encode('utf-8')
        # get @me user city id
        user_province_id = int(
            callme_user_info['user']['province'].encode('utf-8'))
        user_city_id = int(
            callme_user_info['user']['city'].encode('utf-8'))

        # get city name(provinces_citys: list)
        t = requests.get('http://api.t.sina.com.cn/provinces.json')
        provinces_citys = json.loads(t.content)['provinces']
        for each in provinces_citys:
        # if province id == province name: record province name and capital
                if each['id'] == user_province_id:
                    user_capital = each['citys'][0]['1'].encode('utf-8')
                    user_province = each['name'].encode('utf-8')
                    print user_capital, user_province
                    # tem: the city list of each province
                    tem = each['citys']
                    for ever in tem:
                        x = int(ever.keys()[0])
                        if x == user_city_id:
                            user_city_id = ever['%s' % x].encode('utf-8')
                        if user_city_id == '':
                            user_city_id = '你那里是'
        # get user city, user province and user capital
        print user_city_id, user_province, user_capital

        # build weather information to reply ascording to user localtion
        weather_info = get_weather(user_city_id, user_capital)
        date = weather_info[0]['date'].encode('utf-8')
        weather = weather_info[0]['weather'].encode('utf-8')
        temp = weather_info[0]['temperature'].encode('utf-8')
        wind = weather_info[0]['wind'].encode('utf-8')
        t = time.strftime("%Y年%m月%d日 %H时%M分")
        # judge where are weather information from depend on the value of i
        i = weather_info.pop()
        if (i == 0):
            con = '你是想问我天气吗？告诉你哟，%s,%s,现在是%s,\
            今天天气为%s,温度为%s,%s,每一天都是新的~！' % (
                user_city_id, date, t, weather, temp, wind)
        elif (i == 1):
            con = '哎呀我不知道%s是什么样的天气啊~不过省会%s今天是%s，\
            现在天气%s，温度为%s,%s,Every day is a new day~!' % (
                user_city_id, user_capital, t, weather, temp, wind)
        else:
            con = '虽然你召唤我了，可是你好像不在中国呀，\
            我也没办法告诉你天气啦，不过可以和你说首都现在是%s，天气%s，\
            温度为%s，%s，The summer is coming~！' % (
                t, weather, temp, wind)

        # record @me weibo information
        call_me_log = '%s create on %s Content: %s.\n' % (
            name, created_at, last_callme_weibo_content
        )
        call_log(call_me_log, call_me_weibo='1')

        # Reply weibo
        print (' Reply Processing...')
        try:
            print ('    Reply to %s.\n') % name
            update_localtion_date(last_cwi, last_cwi='1')
            client.comments.create.post(
                id=last_cwi, comment=con)
        except Exception as e:
            print ('发送失败：%s.\n' % str(e))

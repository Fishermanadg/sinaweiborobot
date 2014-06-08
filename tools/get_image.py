#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import re
import requests
import random


# get random image
def get_img():
    # get image url
    re_imghtml = re.compile(r'href="(http://www.topit.me/item/\d{5,8})"><img')
    # get img url
    re_img = re.compile(r"href='(.*\.jpg)' download")
    page_id = random.randint(1, 10)
    img_id = random.choice(range(20))
    try:
        html = requests.get('http://www.topit.me/?p=%s' % page_id)
        img_page = re.findall(re_imghtml, html.content)[img_id]

        img = requests.get(img_page).content
        img_url = re.findall(re_img, img)[0]
        with open('./img/temp_image.jpg','wb') as f:
            f.write(requests.get(img_url).content)
    except:
        print ('Get image have an error!')
    return None


# get bing image every day
def get_bing_img():
    re_bing = re.compile(r"g_img={url:'(.*?)'")
    try:
        bing_html = requests.get('http://cn.bing.com')
        Bing_img_url = re.findall(re_bing, bing_html.content)[0]
        with open('./img/Bing_img.jpg','wb') as f:
            f.write(requests.get(Bing_img_url).content)
    except:
        print ('Get Bing image have an error!')
    return None
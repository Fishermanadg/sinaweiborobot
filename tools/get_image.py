#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import urllib
import re
import requests
import random
from tools import call_log


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
        # image_web_url
        p = 'The URL of image web: %s.\n' % img_page
        img_url = re.findall(re_img, requests.get(img_page).content)[0]
        # image_url
        q = 'The URL of image: %s.\n' % img_url
        # logging
        l = p + q
        call_log(q)
        urllib.urlretrieve(img_url, './img/temp_image.jpg')
    except e:
        print ('Get image have an error! Error: %s' % str(e))
    return None


# get bing image every day
def get_bing_img():
    re_bing = re.compile(r"g_img={url:'(.*?)'")
    bing_html = requests.get('http://cn.bing.com')
    Bing_img_url = re.findall(re_bing, bing_html.content)[0]
    urllib.urlretrieve(Bing_img_url, './img/Bing_img.jpg')
    # logging
    l = 'The URL of Bing_image web: %s.' % Bing_img_url
    # call_log(l)
    return None

#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import urllib
import urllib2
from weibo import APIClient
import config


# userID = 'qgqing777@126.com'
user = config.user_email
password = config.user_password
API_KEY = config.app_key
API_SECRET = config.app_secret
CALLBACK_URL = config.callback_url
client = APIClient(API_KEY, API_SECRET, CALLBACK_URL)
referer_url = client.get_authorize_url()

postdata = {
    "client_id": API_KEY,
    "redirect_uri": CALLBACK_URL,
    "isLoginSina": "0",
    "userId": user,
    "passwd": password,
    "action": "submit",
    "response_type": "code",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36",
    "Host": "api.weibo.com",
    "Referer": referer_url
}


def login():
    try:
        tem = urllib2.Request(
            url=referer_url, data=urllib.urlencode(postdata), headers=headers)
        resp = urllib2.urlopen(tem)
        # get access_token
        t = resp.geturl()[-32:]
        r = client.request_access_token(t)
        client.set_access_token(r.access_token, r.expires_in)
        print ('Login Success!')
    except:
        print ('An Error!Please checking login!')
    return client

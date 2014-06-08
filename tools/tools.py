#!/usr/bin/env python
# --*-- coding:utf-8 --*--


def update_localtion_date(date, last_cwi='0', last_cci='0'):
    # update localtion date
    if (last_cwi == '1' or last_cci == '1'):
        with open('./res/weibo_id.txt', 'r') as f:
            a = f.readlines()
        if (last_cwi == '1'):
            a[0] = str(date) + '\n'
        else:
            a[1] = str(date)
        with open('./res/weibo_id.txt', 'w') as f:
            f.writelines(a)
    else:
        print ('Please specify which of the data update!')
    return None



def call_log(log, error='0', call_me_weibo='0', comments_weibo='0'):
    # logging
    if (error == '1'):
        try:
            with open('./res/errors.log', 'a') as e:
                e.write(log)
        except IOError as e:
            print('Error logging have errors: %s!\n' % str(e))
    elif (call_me_weibo == '1'):
        try:
            with open('./res/call_me_weibo.log', 'a') as c:
                c.write(log)
        except IOError as e:
            print('Call me weibo logging have errors: %s!\n' % str(e))
    elif (comments_weibo == '1'):
        try:
            with open('./res/comments_weibo.log', 'a') as w:
                w.write(log)
        except IOError as e:
            print('Comments weibo logging have errors: %s!\n' % str(e))
    else:
        try:
            with open('./res/send_weibo.log', 'a') as s:
                s.write(log)
        except IOError as e:
            print('Send weibo logging have errors: %s!\n' % str(e))
    return None

#!/usr/bin/env python
# --*-- coding:utf-8 --*--
from reply_weibo import reply_weibo
from reply_comments import reply_comments
from reply_atme_comments import reply_atme_comments
from tools import call_log, update_localtion_date


def reply(client=None):
    if client == None:
        print ('Pleass login in!!')
    else:
        # get @me weibo metadate
        last_callme_weibo_list = client.statuses.mentions.get()
        last_callme_weibo_id = last_callme_weibo_list['statuses'][0]['id']
        last_callme_weibo_content = last_callme_weibo_list[
            'statuses'][0]['text'].encode('utf-8')

        # get comments to me metadate
        last_callme_commentlist = client.comments.to_me.get(
            filter_by_author=1)['comments'][0]
        last_callme_comment_id = last_callme_commentlist['id']
        last_callme_comment_username = last_callme_commentlist[
            'user']['name'].encode('utf-8')
        last_callme_comment_created_at = last_callme_commentlist[
            'created_at'].encode('utf-8')
        last_callme_comment_content = last_callme_commentlist[
            'text'].encode('utf-8')
        last_comment_weibo_id = last_callme_commentlist['status']['id']

        # get atme comments metadte
        last_atme_comment = client.comments.mentions.get()
        last_atme_comment_id = last_atme_comment['comments'][0]['id']
        last_atme_comment_username = last_atme_comment[
            'comments'][0]['user']['name'].encode('utf-8')
        last_atme_comment_created_on = last_atme_comment[
            'comments'][0]['created_at'].encode('utf-8')
        last_atme_comment_content = last_atme_comment[
            'comments'][0]['text'].encode('utf-8')
        last_atme_comment_weibo_id = last_atme_comment[
            'comments'][0]['status']['id']

        # read last @me weibo id ,last comments id and last atme comment id
        with open('./res/weibo_id.txt', 'rb') as q:
            t = q.readlines()
            record_callme_weibo_id = t[0]
            record_calllme_comments_id = t[1]
            record_atme_comment_id = t[2]

        last_cwi = last_callme_weibo_id
        record_cwi = long(record_callme_weibo_id)
        last_cci = last_callme_comment_id
        record_cci = long(record_calllme_comments_id)
        last_aci = last_atme_comment_id
        record_aci = long(record_atme_comment_id)
        # print ('Last weibo id:', last_cwi,
        #        'localtion weibo id:', record_cwi)
        # print ('Last comment id:', last_cci,
        #        'localtion comment id:', record_cci)
        # print ('Lasr atme comment id:', last_aci,
        #        'localtion atme comment id: ', record_aci)
        # reply @me weibo
        if (last_cwi >= record_cwi):
            if (last_cwi == record_cwi):
                print ('最新@我的微博已回复.')
            else:
                reply_weibo(client,
                            last_cwi,
                            last_callme_weibo_content)
        else:
            update_localtion_date(last_cwi, last_cwi='1')
            print ('Have an @me weibo be deleted!\n')
            p = 'Have an @me weibo be deleted' + '\n'
            call_log(p, call_me_weibo='1')
        # reply comments to me
        if (last_cci >= record_cci):
            if (last_cci == record_cci):
                print ('最新收到的评论已回复.')
            else:
                reply_comments(
                    client,
                    last_cci,
                    last_comment_weibo_id,
                    last_callme_comment_username,
                    last_callme_comment_created_at,
                    last_callme_comment_content)
        else:
            update_localtion_date(last_cci, last_cci='1')
            print ('Have an comment to me be deleted!\n')
            p = 'Have an comment to me be deleted!' + '\n'
            call_log(p, call_me_weibo='1')
        # reply atme comments
        if (last_aci >= record_aci):
            if (last_aci == record_aci):
                print ('最新@我的评论已回复.')
            else:
                reply_atme_comments(
                    client,
                    last_aci,
                    last_atme_comment_weibo_id,
                    last_atme_comment_username,
                    last_atme_comment_created_on,
                    last_atme_comment_content)
        else:
            update_localtion_date(last_aci, last_aci='1')
            print ("Have an @me comment be deleted!\n")
            p = 'Have an @me comment be deleted!' + '\n'
            call_log(p, call_me_weibo='1')
    return None

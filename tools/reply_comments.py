#!/usr/bin/env python
# --*-- coding:utf-8 --*--
from tools import call_log, update_localtion_date


def reply_comments(client,
                   last_cci,
                   last_comment_weibo_id,
                   last_callme_comment_username,
                   last_callme_comment_created_at,
                   last_callme_comment_content):
    if (client == None
            or last_cci == None
            or last_comment_weibo_id == None
            or last_callme_comment_username == None
            or last_callme_comment_created_at == None
            or last_callme_comment_content == None):
        print ("Reply comment error,please checking.")
    else:
        # record comment information
        comments_log = '%s create on %s Content: %s.\n' % (
            last_callme_comment_username,
            last_callme_comment_created_at,
            last_callme_comment_content)
        call_log(comments_log, comments_weibo='1')
        try:
            print ("Reply comment to me from %s.\n" %
                   last_callme_comment_username)
            # update localtion data
            update_localtion_date(last_cci, last_cci='1')
            client.comments.reply.post(
                cid=last_cci, id=last_comment_weibo_id, comment='Hello!')
            print ('Reply Success!\n')
        except Exception as e:
            print ('Reply error: %s' % str(e))

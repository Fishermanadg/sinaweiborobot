#!/usr/bin/env python
# --*-- coding:utf-8 --*--
from tools import call_log, update_localtion_date


def reply_atme_comments(client,
                        last_aci,
                        last_atme_comment_weibo_id,
                        last_atme_comment_username,
                        last_atme_comment_created_on,
                        last_atme_comment_content):
    if (client == None
            or last_aci == None
            or last_atme_comment_weibo_id == None
            or last_atme_comment_username == None
            or last_atme_comment_created_on == None
            or last_atme_comment_content == None):
        print ("Reply @me comment error,please checking.")
    else:
        # record comment information
        comments_log = '%s create on %s Content: %s.\n' % (
            last_atme_comment_username,
            last_atme_comment_created_on,
            last_atme_comment_content)
        call_log(comments_log, comments_weibo='1')
        try:
            print ("Reply @me comment from %s..." %
                   last_atme_comment_username)
            # update localtion data
            update_localtion_date(last_aci, last_aci='1')
            client.comments.reply.post(
                cid=last_aci,
                id=last_atme_comment_weibo_id,
                comment='hey~thanks@ me!')
            print ('Reply Success!\n')
        except Exception as e:
            print ('Reply error: %s' % str(e))

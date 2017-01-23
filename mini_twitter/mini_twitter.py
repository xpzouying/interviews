# -*- coding: utf8 -*-


'''
    实现一个迷你的推特，支持下列几种方法
    1.postTweet(user_id, tweet_text). 发布一条推特.
    2.getTimeline(user_id). 获得给定用户最新发布的十条推特，按照发布时间从最近的到之前排序
    3.getNewsFeed(user_id). 获得给定用户的朋友或者他自己发布的最新十条推特，从发布时间最近到之前排序
    4.follow(from_user_id, to_user_id). from_user_id 关注 to_user_id.
    5.unfollow(from_user_id, to_user_id). from_user_id 取消关注 to_user_id.

    样例
    postTweet(1, "LintCode is Good!!!")
    >> 1
    getNewsFeed(1)
    >> [1]
    getTimeline(1)
    >> [1]
    follow(2, 1)
    getNewsFeed(2)
    >> [1]
    unfollow(2, 1)
    getNewsFeed(2)
    >> []

    http://www.lintcode.com/zh-cn/problem/mini-twitter/
'''


'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''

from tweets import Tweet


class MiniTwitter:

    def __init__(self):
        # initialize your data structure here.


    # @param {int} user_id
    # @param {str} tweet
    # @return {Tweet} a tweet
    def postTweet(self, user_id, tweet_text):
        # Write your code here


    # @param {int} user_id
    # return {Tweet[]} 10 new feeds recently
    # and sort by timeline
    def getNewsFeed(self, user_id):
        # Write your code here


    # @param {int} user_id
    # return {Tweet[]} 10 new posts recently
    # and sort by timeline
    def getTimeline(self, user_id):
        # Write your code here


    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id follows to_user_id
    def follow(self, from_user_id, to_user_id):
        # Write your code here


    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id unfollows to_user_id
    def unfollow(self, from_user_id, to_user_id):
        # Write your code here

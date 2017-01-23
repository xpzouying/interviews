# -*- coding: utf8 -*-


class Tweet:
    tweets = []

    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id

        t = (user_id, tweet_text)
        cls.tweets.append(t)

        return t

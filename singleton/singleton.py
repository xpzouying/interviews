# -*- coding: utf8 -*-


class Singleton(object):
    instance = None

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = Singleton()

        return cls.instance

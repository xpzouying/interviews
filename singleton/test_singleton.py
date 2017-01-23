# -*- coding: utf8 -*-


from unittest import TestCase
from singleton import Singleton


class SingletonTestCase(TestCase):

    def test_singleton(self):

        inst1 = Singleton.get_instance()
        inst2 = Singleton.get_instance()

        self.assertEqual(inst1, inst2)

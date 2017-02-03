# -*- coding: utf8 -*-

import unittest


"""
    Ref:
        - https://www.toptal.com/python/interview-questions

"""


class PythonBasicTestCase(unittest.TestCase):

    def test_list_with_default_value(self):
        def extendList(val, list=[]):
            list.append(val)
            return list

        list1 = extendList(10)
        list2 = extendList(123,[])
        list3 = extendList('a')

        print "list1 = %s" % list1
        print "list2 = %s" % list2
        print "list3 = %s" % list3

        # NOTE: list1 is equal list3
        self.assertEqual(list1, [10, 'a'])
        self.assertEqual(list2, [123])
        self.assertEqual(list3, [10, 'a'])

# -*- coding: utf8 -*-


"""
    对于数组 [3, 2, 1, 4, 5], 排序后为：[1, 2, 3, 4, 5]
"""

from unittest import TestCase
from sort_integers import *


class SortTestCase(TestCase):

    def test_bubble_sort_by_normal_list(self):
        l = [3, 2, 1, 4, 5]
        sorted_l = bubble_sort(l)
        self.assertEqual(sorted_l, [1, 2, 3, 4, 5])

    def test_bubble_sort_by_empty_list(self):
        l = []
        sorted_l = bubble_sort(l)
        self.assertEqual(sorted_l, [])

    def test_bubble_sort_by_one_element(self):
        l = [1]
        sorted_l = bubble_sort(l)
        self.assertEqual(sorted_l, [1])

    def test_bubble_sort_by_two_element(self):
        l = [2, 1]
        sorted_l = bubble_sort(l)
        self.assertEqual(sorted_l, [1, 2])

    def test_bubble_sort_by_reverse_sort(self):
        l = [5, 4, 3, 2, 1]
        sorted_l = bubble_sort(l)
        self.assertEqual(sorted_l, [1, 2, 3, 4, 5])

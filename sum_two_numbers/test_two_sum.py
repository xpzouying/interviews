# -*- coding: utf8 -*-


from unittest import TestCase

from two_sum import two_sum


class TestTwoSum(TestCase):

    def test_normal_list(self):
        target_lst = [2, 7, 11, 17]
        target_sum = 9
        l = two_sum(target_lst, target_sum)

        self.assertEqual(l, [(0, 1)])


    def test_empty_list(self):
        target_lst = []
        target_sum = 3
        l = two_sum(target_lst, target_sum)

        self.assertEqual(l, [])


    def test_one_element_list(self):
        target_lst = [1]
        target_sum = 3
        l = two_sum(target_lst, target_sum)

        self.assertEqual(l, [])


    def test_two_elements_list(self):
        target_lst = [1, 2]
        target_sum = 3
        l = two_sum(target_lst, target_sum)

        self.assertEqual(l, [(0, 1)])


    def test_multiple_elements_with_multiple_result_list(self):
        target_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target_sum = 10
        l = two_sum(target_lst, target_sum)

        self.assertEqual(l, [(0, 8), (1, 7), (2, 6), (3, 5)])

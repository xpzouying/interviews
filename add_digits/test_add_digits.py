

from unittest import TestCase

from add_digits import add_digits


class AddDigitsTestCase(TestCase):

    def test_one_digit(self):
        res = add_digits(8)

        self.assertEqual(res, 8)

    def test_two_digits(self):
        res = add_digits(38)

        """
        3 + 8 ==> 11
        1 + 1 ==> 2
        """

        self.assertEqual(res, 2)

    def test_three_digits(self):
        res = add_digits(935)

        """
        9 + 3 + 5 ==> 17
        1 + 7 ==> 8
        """
        self.assertEqual(res, 8)

    def test_more_than_three_digits(self):
        res = add_digits(9678)

        """
        9 + 6 + 7 + 8 ==> 30
        3 + 0 ==> 3
        """

        self.assertEqual(res, 3)

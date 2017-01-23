# -*- coding: utf8 -*-

"""Given a non-negative integer num,
    repeatedly add all its digits until the result has only one digit.


样例
    Given num = 38.
    The process is like: 3 + 8 = 11, 1 + 1 = 2.
    Since 2 has only one digit, return 2.

"""


def sum_digits(digits):
    sum = 0

    # if digits < 10:
    #     return digits

    # div_res = digits / 10
    div_res = digits
    while div_res != 0:

        # if more than double digit
        mod_res = div_res % 10
        sum += mod_res
        div_res = div_res // 10

    return sum


def add_digits(digits):
    sum = digits

    while sum >= 10:
        sum = sum_digits(sum)

    return sum

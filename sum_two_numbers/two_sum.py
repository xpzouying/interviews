# -*- coding: utf8 -*-


def two_sum(lst, sum):
    """Sum two number from ordered list, if two number sum equal sum, then return it.

    @input:
        lst: list of number
        sum: expect sum
    @return:
        list of index.

    Example:
    input: [1, 2, 3, 5, 9]
    input: 7
    output: [(1, 3)]

    Tips:
    index of begin and last,
    begin index forward from begin to end,
    end index backward from end to begin.
    """

    l = []

    begin = 0
    # end = len(lst)-1

    for begin in range(len(lst)):
        expect_num = sum - lst[begin]

        second_index = begin + 1
        # while second_index < len(lst) - 1:
        for second_index in range(begin+1, len(lst)):
            # if number is greater than expect_num, then break
            if lst[second_index] > expect_num:
                break
            elif lst[second_index] == expect_num:
                # if equal, then find it
                l.append((begin, second_index))
            else:
                continue

    return l

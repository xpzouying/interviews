# -*- coding: utf8 -*-


def bubble_sort(l):
    new_list = l[:]
    length = len(new_list) - 1

    sorted = False

    while not sorted:
        sorted = True

        for i in range(length):
            if new_list[i] > new_list[i+1]:
                # swap i and i+1
                new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
                sorted = False

    return new_list

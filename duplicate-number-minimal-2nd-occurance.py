#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.
"""


import unittest

def find_duplicate(a):
    b = {}
    c = {}
    for i, j in enumerate(a):
        if j in b:
            if b[j] == 1:
                continue
            if b[j] == 0:
                b[j] = 1
                c[j] = i
        else:
            b[j] = 0
    try:
        return min(c, key=c.get)
    except ValueError:
        return -1


class DuplicateTestCase(unittest.TestCase):
    def test_duplicate(self):
        self.assertEqual(3, find_duplicate([2, 1, 3, 5, 3, 2]))
        self.assertEqual(-1, find_duplicate([2, 4, 3, 5, 1]))



if __name__ == "__main__":
    unittest.main()

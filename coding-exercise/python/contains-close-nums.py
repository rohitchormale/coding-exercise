#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
if 2 elements from given list such that, 
list[i] = list[k] i.e. duplicate
abs(i - j) <= k
"""

from collections import defaultdict
from itertools import izip


def foo(nums, k):
    # duplicate check
    if len(nums) == len(set(nums)):
        return False
    
    # find duplicates
    lookup = defaultdict(list)
    for i, j in enumerate(nums):
        lookup[j].append(i)

    # if duplicates or more, calculate differences between adjusant elements.
    # if diff <= k, return True
    for l in lookup.values():
        if len(l) < 2:
            continue
        if [ c for c in [abs(a-b) for a, b in izip(l[:-1], l[1:])] if c <= k ]:
            return True
    return False
         

import unittest
class FooTestCase(unittest.TestCase):
    def test_foo(self):
        nums1 = [0, 1, 2, 3, 5, 2] 
        k1 = 3
        nums2 = [0, 1, 2, 3, 5, 2]
        k2 = 2
        self.assertEqual(foo(nums1, k1), True)
        # self.assertEqual(foo(nums2, k2), False)


if __name__ == '__main__':
    unittest.main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Rotate nxn matrix in 90% clockwise
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
    
output 
[[7, 4, 1]
 [8, 5, 2]
 [9, 6, 3]]
"""


from itertools import izip
def foo(a):
    for i in izip(*a):
        print i
    return [ list(reversed(i)) for i in izip(*a) ]


import unittest
class FooTestCase(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(foo([[1,2,3], [4,5,6], [7,8,9]]), [[7,4,1], [8,5,2], [9,6,3]])


if __name__ == '__main__':
    unittest.main()

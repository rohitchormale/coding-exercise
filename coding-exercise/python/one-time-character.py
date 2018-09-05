#!/usr/bin/env python
# -*- coding: utf-8 -*-



"""
For given lower case string, find first character appeared only one time.
Return '_' if not such character
"""

import unittest



import string

def foo(s):
    occure = {}
    for i in string.lowercase:
        a = string.find(s, i)
        b = string.rfind(s, i)
        if a == b and a != -1:
            occure[i] = a
    
    if not occure:
        return '_'
    return min(occure, key=occure.get)


class FooTestCase(unittest.TestCase):
    def test_foo(self):
        self.assertEqual('_', foo('aaabbbccaa'))
        self.assertEqual('f', foo('aaabbbccadafsd'))

if __name__ == "__main__":
    unittest.main()

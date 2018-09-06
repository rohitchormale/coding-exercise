#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
True if string[i] = string[j] and pattersn[i] != patterns[j]
False if string[i] != string[j] and patterns[i] != patterns[j]
"""


def foo(strings, patterns):
    lookup = {}
    rlookup = {}
    for i, j in enumerate(strings):
        if j in lookup and lookup[j] != patterns[i]:
                return False
        elif patterns[i] in rlookup and  rlookup[patterns[i]] != j:
                return False
        else:
            lookup[j] = patterns[i]
            rlookup[patterns[i]] = j
    return True


import unittest
class FooTestCase(unittest.TestCase):
    def test_foo(self):
        strings1 = ["cat", "dog", "dog"]
        patterns1 = ["a", "b", "b"]
        strings2 = ["cat", "dog", "doggy"]
        patterns2 = ["a", "b", "b"]
        strings3 = ["cat", "dog", "dog"]
        pattern3 = ["a", "b", "c"]
        self.assertEqual(foo(strings1, patterns1), True)
        self.assertEqual(foo(strings2, patterns2), False)
        self.assertEqual(foo(strings3, patterns3), False)


if __name__ == '__main__':
    unittest.main()


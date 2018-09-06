#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
crypt = ["SEND", "MORE", "MONEY"]
solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]

condition 1 = addition of first 2 equal last one
    "SEND" + "MORE" = "MONEY"
    9567 + 1085 = 10652 return True
condition 2 = should not be leading zeros
    054 + 091 = 145 return False

"""


def foo(crypt, solution):
    solm = { i[0]: i[1] for i in solution }
    rsolm = { v: k for k, v in solm.items() } 
    c1 = "".join([ solm[i] for i in crypt[0] ])
    if c1.startswith('0') and len(c1) > 1: return False
    c2 = "".join([ solm[i] for i in crypt[1] ]) 
    if c2.startswith('0') and len(c1) > 1: return False
    c3 = "".join([ solm[i] for i in crypt[2] ])
    if c3.startswith('0') and len(c1) > 1: return False
    if int(c1) + int(c2) != int(c3):
        return False
    return True


import unittest
class FooTestCase(unittest.TestCase):
    def test_foo_true(self):
        solution = [['O', '0'],
                    ['M', '1'],
                    ['Y', '2'],
                    ['E', '5'],
                    ['N', '6'],
                    ['D', '7'],
                    ['R', '8'],
                    ['S', '9']]
        crypt = ["SEND", "MORE", "MONEY"]
        self.assertEqual(foo(crypt, solution), True)


    def test_foo_false(self):
         crypt = ["TEN", "TWO", "ONE"]
         solution = [['O', '1'],
                     ['T', '0'],
                     ['W', '9'],
                     ['E', '5'],
                     ['N', '4']]
         self.assertEqual(foo(crypt, solution), False)

    def test_foo_leading_zeros(self):
        crypt = ["A", "A",  "A"]
        solution = [["A", "0"]]
        self.assertEqual(foo(crypt, solution), True)


if __name__ == '__main__':
    unittest.main()





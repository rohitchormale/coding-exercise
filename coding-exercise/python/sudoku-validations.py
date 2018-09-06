#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Check if given grid is valid Sudo grid
"""

from itertools import izip

def foo(grid):
    # chck duplicates horizontally
    for row in grid:
    	crow = [ i for i in row if i != '.']
    	if len(crow) != len(set(crow)):
    		return False
    # check duplicates vertically
    vgrid = izip(*grid) 
    for row in vgrid:
    	crow = [ i for i in row if i != '.']
    	if len(crow) != len(set(crow)):
    		return False
    # check duplicates in 3x3 squre
    l = []
    for i in grid:
        l.append(i[0:3])
        l.append(i[3:6])
        l.append(i[6:9])

    def bar(a, b, c):
        return [ i for i in l[a] + l[b] + l[c] if i != '.']
    
    ll = [(0,3,6), (1,4,7), (2,5,8),
        (9, 12, 15), (10, 13, 16), (11, 14, 17),
        (18, 21, 24), (19, 22, 25), (20, 23, 26)]
    for i in ll:
        j = bar(i[0], i[1], i[2])
        if len(j) != len(set(j)):
            return False
    return True    

import unittest
grid1 = [['.', '.', '.',   '1', '4', '.',   '.', '2', '.'],
        ['.', '.', '6',   '.', '.', '.',   '.', '.', '.'],
        ['.', '.', '.',   '.', '.', '.',   '.', '.', '.'],

        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],

        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

grid2 = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],

        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],

        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

class FooTestCase(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(foo(grid1), True)
        self.assertEqual(foo(grid2), True)


if __name__ == '__main__':
    unittest.main()


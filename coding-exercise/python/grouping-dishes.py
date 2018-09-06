#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
  dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

output =  [["Cheese", "Quesadilla", "Sandwich"],
            ["Chicken", "Chicken Curry", "Quesadilla"],
            ["Nuts", "Fried Rice", "Salad"],
            ["Onions", "Fried Rice", "Pasta"]]

constrain - not big data
"""

from collections import defaultdict
def foo(dishes):
    ingredients = defaultdict(list)
    for dish in dishes:
        for i in dish[1:]:
            ingredients[i].append(dish[0])
    sorted_ingredients = []
    for i in sorted(ingredients):
        if len(ingredients[i]) > 1: 
            temp =  sorted(ingredients[i])
            temp.insert(0, i)
            sorted_ingredients.append(temp)
    return sorted_ingredients
        


import unittest
class FooTestCase(unittest.TestCase):
    def test_foo(self):
        dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
                    ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
                    ["Quesadilla", "Chicken", "Cheese", "Sauce"],
                    ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
        output = [["Cheese", "Quesadilla", "Sandwich"],
                  ["Salad", "Salad", "Sandwich"],
                  ["Sauce", "Pizza", "Quesadilla", "Salad"],
                  ["Tomato", "Pizza", "Salad", "Sandwich"]]
        self.assertEqual(foo(dishes), output)


if __name__ == '__main__':
    unittest.main()


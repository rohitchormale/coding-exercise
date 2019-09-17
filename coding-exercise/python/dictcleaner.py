#!/usr/bin/env python3
"""
Dict Cleaner - Remove empty/None items from dict.

Why are interviews so horrible ? When this question asked in interview, I blanked out. And today in this beautiful morning, I implemented it with ease. 
"""


def dict_cleaner(d):
    subtemp = {}
    for i, j in d.items():
        if j is None or (isinstance(j, str) and j.strip()) == "":
            continue
        elif isinstance(j, list):
            clist = [a for a in j if a]
            if not clist:
                continue
            subtemp[i] = clist
        elif isinstance(j, dict):
            cdict = dict_cleaner(j)
            if not cdict:
                continue
            subtemp[i] = cdict
        else:
            subtemp[i] = j
    return subtemp


import unittest
class DictCleanerTestCase(unittest.TestCase):
    def test_dict_cleaner(self):
        a = {"foo": "bar", "bar": [1, 2, ''], "baz": {"foo": "", "bar": [1, 2, '']}, "qux": ""}
        a_cleaned = {"foo": "bar", "bar": [1, 2], "baz": {"bar": [1, 2]}}

        b = {"foo": "bar", "bar": [1, 2, ''], "baz": {"foo": "", "bar": [1, 2, ''], "qux": {"foo": "bar", "bar": ""}}, "qux": ""}
        b_cleaned = {"foo": "bar", "bar": [1, 2], "baz": {"bar": [1, 2], "qux": {"foo": "bar"}}}

        c = {"foo": {"bar": {"baz": {"qux": ""}}}}
        c_cleaned = {}

        d = {"foo": 0, "bar": "", "baz": "    ", "qux": None}
        d_cleaned = {"foo": 0}


        self.assertEqual(dict_cleaner(a), a_cleaned)
        self.assertEqual(dict_cleaner(b), b_cleaned)
        self.assertEqual(dict_cleaner(c), c_cleaned)
        self.assertEqual(dict_cleaner(d), d_cleaned)


if __name__ == "__main__":
    unittest.main()




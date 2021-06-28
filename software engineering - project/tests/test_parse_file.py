#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
import os
from parser.parser import parse_file


class TestStringMethods(unittest.TestCase):

    def test_parse_file(self):
        path_dir = 'test_dir'
        os.mkdir(path_dir)

        path1 = os.path.join(path_dir, 'test_file1.py')

        f1 = open(path1, "w+")
        f1.write("# !/usr/bin/env python\n")
        f1.write("# -*- coding: utf-8 -*-\n")
        f1.write("\n\n")
        f1.write("def test():\n")
        f1.write("\tpass")
        f1.write("\n\n")
        f1.write("def test2():\n")
        f1.write("\ttest()")
        f1.write("\n\n")
        f1.write("def test3():\n")
        f1.write("\ttest()\n")
        f1.write("\ttest2()")
        f1.write("\n\n")

        f1.close()
        file = parse_file(path1)

        self.assertEqual(len(file.functions), 3)
        os.remove(path1)
        os.rmdir(path_dir)


if __name__ == "__main__":
    unittest.main()

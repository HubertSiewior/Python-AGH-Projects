#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os
from H1 import get_file_paths as gfp


class TestStringMethods(unittest.TestCase):

    def test_get_paths(self):
        path_dir = 'test_dir'
        os.mkdir(path_dir)

        path1 = os.path.join(path_dir, 'test_file1.py')
        path2 = os.path.join(path_dir, 'test_file2.txt')
        path3 = os.path.join(path_dir, 'test_file3.py')

        f1 = open(path1, "w+")
        f2 = open(path2, "w+")
        f3 = open(path3, "w+")

        f1.close()
        f2.close()
        f3.close()

        self.assertEqual(gfp.get_paths(path_dir), [path1, path3])
        os.remove(path1)
        os.remove(path2)
        os.remove(path3)
        os.rmdir(path_dir)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from H1.get_module_usage import FileNode


class TestStringMethods(unittest.TestCase):
    def test_to_array(self):
        file_node = FileNode("name", "module_name", 2, None, None, None, None, None, None)
        array = file_node.to_array()
        self.assertEqual(array, ["name", "module_name", 2, None, None, None, None, None, None])


if __name__ == "__main__":
    unittest.main()
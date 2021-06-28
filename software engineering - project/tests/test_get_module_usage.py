import os
import unittest
from H1 import get_module_usage as gmu


class TestStringMethods(unittest.TestCase):

    def test_get_node_data(self):
        path_dir = '../test_dir2'
        os.mkdir(path_dir)

        path1 = os.path.join(path_dir, 'test_file1.py')

        f1 = open(path1, "w+")
        f1.write("# !/usr/bin/env python\n")
        f1.write("# -*- coding: utf-8 -*-\n")
        f1.write("\n\n")
        f1.write("import os\n")
        f1.write("\n\n")
        f1.write("def testa():\n")
        f1.write("\tpass")
        f1.write("\n\n")
        f1.write("def testb():\n")
        f1.write("\ttesta()\n")
        f1.write("\n\n")

        f1.close()

        path2 = os.path.join(path_dir, 'test_file2.py')
        f2 = open(path2, "w+")
        f2.write("# !/usr/bin/env python\n")
        f2.write("# -*- coding: utf-8 -*-\n")
        f2.write("\n\n")
        f2.write("import os\n")
        f2.write("\n\n")
        f2.write("def testc():\n")
        f2.write("\tpass")
        f2.write("\n\n")
        f2.write("def testd():\n")
        f2.write("\ttestc()\n")
        f2.write("\n\n")

        f2.write("def main(argument_path=None):\n")
        f2.write("\tteste()\n")
        f2.write("\n\n")
        f2.write("if __name__ == '__main__':\n")
        f2.write("\tmain()\n\n")

        f2.close()

        files_with_modules = gmu.get_files_with_modules(path_dir, False)
        nodes = gmu.get_node_data(path_dir, files_with_modules, False)

        expected_result_1 = ['test_file1.py', 'test_dir2', 105, True, '../test_dir2/test_file1.py', ['testa', 'testb'], [[None, 'os', None, '/usr/lib/python3.5/os.py']], ['testa'], [None, 0]]
        expected_result_2 = ['test_file2.py', 'test_dir2', 182, True, '../test_dir2/test_file2.py', ['main', 'testc', 'testd'], [[None, 'os', None, '/usr/lib/python3.5/os.py']], ['teste', 'main', 'testc'], [0, None]]

        self.assertEqual(nodes[0].to_array(), expected_result_1)
        self.assertEqual(nodes[1].to_array(), expected_result_2)

        os.remove(path1)
        os.remove(path2)
        os.rmdir(path_dir)

    def test_to_simple_array(self):
        file_node = gmu.FileNode("name", "module_name", 2, None, None, None, None, None, None)
        array = file_node.to_simple_array()
        self.assertEqual(array, ["name", 2, None])

    def test_to_array(self):
        file_node = gmu.FileNode("name", "module_name", 2, None, None, None, None, None, None)
        array = file_node.to_array()
        self.assertEqual(array, ["name", "module_name", 2, None, None, None, None, None, None])


if __name__ == '__main__':
    unittest.main()

import unittest
import os
from H2 import get_function_usage as gfu
from H1 import get_file_paths as gfp


class Test_get_function_usage(unittest.TestCase):

    def test_get_function_data_with_one_file_one_directory(self):
        path_dir = 'test_dir'
        os.mkdir(path_dir)

        path1 = os.path.join(path_dir, 'test_file1.py')

        f1 = open(path1, "w+")
        f1.write("# !/usr/bin/env python\n")
        f1.write("# -*- coding: utf-8 -*-\n")
        f1.write("\n\n")
        f1.write("import os\n")
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
        function_data = gfu.get_function_data(path_dir, gfp.get_paths(path_dir))

        expected_data1 = ['test_file1.test', 18, [None, 0, 0]]
        expected_data2 = ['test_file1.test2', 21, [1, None, 0]]
        expected_data3 = ['test_file1.test3', 30, [1, 1, None]]

        self.assertEqual(function_data[0].get_data(), expected_data1)
        self.assertEqual(function_data[1].get_data(), expected_data2)
        self.assertEqual(function_data[2].get_data(), expected_data3)

        os.remove(path1)
        os.rmdir(path_dir)

    def test_get_function_data_with_multiple_files_in_one_directory(self):
        path_dir = 'test_dir2'
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

        function_data = gfu.get_function_data(path_dir, gfp.get_paths(path_dir))

        expected_data1 = ['test_file1.testa', 19, [None, 0, 0, 0, 0]]
        expected_data2 = ['test_file1.testb', 22, [1, None, 0, 0, 0]]
        expected_data3 = ['test_file2.main', 39, [0, 0, None, 0, 0]]
        expected_data4 = ['test_file2.testc', 19, [0, 0, 0, None, 0]]
        expected_data5 = ['test_file2.testd', 22, [0, 0, 0, 1, None]]

        self.assertEqual(function_data[0].get_data(), expected_data1)
        self.assertEqual(function_data[1].get_data(), expected_data2)
        self.assertEqual(function_data[2].get_data(), expected_data3)
        self.assertEqual(function_data[3].get_data(), expected_data4)
        self.assertEqual(function_data[4].get_data(), expected_data5)

        os.remove(path1)
        os.remove(path2)
        os.rmdir(path_dir)

    def test_get_function_data_with_multiple_directories(self):
        path_dir1 = 'test_dir3'
        path_dir2 = 'test_dir4'
        path_dir3 = 'test_dir5'

        os.mkdir(path_dir1)
        os.mkdir(os.path.join(path_dir1, path_dir2))
        os.mkdir(os.path.join(path_dir1, path_dir3))

        path1 = os.path.join(os.path.join(path_dir1, path_dir2), 'test_file1.py')

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

        path2 = os.path.join(os.path.join(path_dir1, path_dir3), 'test_file2.py')

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

        function_data = gfu.get_function_data(path_dir1, gfp.get_paths(path_dir1))


        expected_data1 = ['test_file1.testa', 19, [None, 0, 0, 0, 0]]
        expected_data2 = ['test_file1.testb', 22, [1, None, 0, 0, 0]]
        expected_data3 = ['test_file2.main', 39, [0, 0, None, 0, 0]]
        expected_data4 = ['test_file2.testc', 19, [0, 0, 0, None, 0]]
        expected_data5 = ['test_file2.testd', 22, [0, 0, 0, 1, None]]

        self.assertEqual(function_data[0].get_data(), expected_data1)
        self.assertEqual(function_data[1].get_data(), expected_data2)
        self.assertEqual(function_data[2].get_data(), expected_data3)
        self.assertEqual(function_data[3].get_data(), expected_data4)
        self.assertEqual(function_data[4].get_data(), expected_data5)

        os.remove(path1)
        os.remove(path2)
        os.rmdir(os.path.join(path_dir1, path_dir2))
        os.rmdir(os.path.join(path_dir1, path_dir3))
        os.rmdir(path_dir1)

if __name__ == '__main__':
    unittest.main()

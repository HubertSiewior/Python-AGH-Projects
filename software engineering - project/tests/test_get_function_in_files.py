import os
import unittest
from H6 import get_functions_in_files


class TestStringMethods(unittest.TestCase):

    def test_get_functions_in_files(self):
        path_dir = 'test_dir'
        path_dir2 = os.path.join(path_dir, 'test_dir2')

        os.mkdir(path_dir)
        os.mkdir(path_dir2)
        path1 = os.path.join(path_dir2, 'test_file1.py')
        path2 = os.path.join(path_dir2, 'test_file2.py')
        path3 = os.path.join(path_dir, 'test_file3.py')
        f1 = open(path1, "w+")
        f1.write("def test():\n")
        f1.write("\tpass")
        f2 = open(path2, "w+")
        f2.write("def test1():\n")
        f2.write("\tpass\n")
        f2.write("def main():\n")
        f2.write("\tpass\n")
        f3 = open(path3, "w+")
        f3.write("def test4():\n")
        f3.write("\tpass\n")
        f1.close()
        f2.close()
        f3.close()
        expected_data1 = [['test_dir', 'test_file3.py'], ['test4']]
        expected_data2 = [['test_dir2', 'test_file1.py'], ['test']]
        expected_data3 = [['test_dir2', 'test_file2.py'], ['test1', 'test_file2.py/main']]
        function_in_files = get_functions_in_files.main(os.path.abspath(path_dir))
        self.assertEqual(function_in_files[0], expected_data1)
        self.assertEqual(function_in_files[1], expected_data2)
        self.assertEqual(function_in_files[2], expected_data3)
        os.remove(path1)
        os.remove(path2)
        os.remove(path3)
        os.rmdir(path_dir2)
        os.rmdir(path_dir)


if __name__ == '__main__':
    unittest.main()

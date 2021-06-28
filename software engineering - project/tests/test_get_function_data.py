import os
import unittest
from H6 import get_functions_in_files as gfif


class Test_get_function_data(unittest.TestCase):
    def test_files_with_no_functions(self):
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

        file_paths = [path1, path2, path3]
        expected_data = [[[path_dir, "test_file1.py"], []], [[path_dir, "test_file2.txt"], []], [[path_dir, "test_file3.py"], []]]

        data = gfif.get_function_data(path_dir, file_paths)

        self.assertEqual(data, expected_data)

        os.remove(path1)
        os.remove(path2)
        os.remove(path3)
        os.rmdir(path_dir)

    def test_files_with_functions(self):
        path_dir = 'test_dir'
        os.mkdir(path_dir)

        path1 = os.path.join(path_dir, 'test_file1.py')

        f1 = open(path1, "w+")

        f1.write("def function():\n\tpass")

        f1.close()

        file_paths = [path1]
        expected_data = [[[path_dir, "test_file1.py"], ["function"]]]

        data = gfif.get_function_data(path_dir, file_paths)

        self.assertEqual(data, expected_data)

        os.remove(path1)
        os.rmdir(path_dir)


if __name__ == '__main__':
    unittest.main()

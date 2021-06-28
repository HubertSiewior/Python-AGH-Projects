#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from H1 import get_file_paths as gfp
from H6 import get_functions_in_files as gfif
from H6 import draw_graphH6 as dg
import sys

def main(argument_path=None):

    if argument_path is None:
        root_dir = os.path.dirname(os.getcwd())
    else:
        root_dir = argument_path
    print(root_dir)
    dirs = gfp.get_paths(root_dir)
    data = gfif.get_function_data(root_dir, dirs)
    print(data)
    try:
        nodes = gfif.main(root_dir)
        dg.main(nodes)
    except IOError:
        print("File with path ", root_dir, "could not be opened")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_path = sys.argv[1]
        main(arg_path)
    else:
        main()

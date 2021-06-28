#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from H2 import get_function_usage as gfu
from H1 import draw_graph as dg
import sys


def main(argument_path=None):
    if argument_path is None:
        path = os.path.dirname(os.getcwd())
    else:
        path = argument_path

    try:
        function_data = gfu.main(path)
        dg.main(function_data)
        print(function_data)
    except IOError:
        print("File with path", argument_path, "could not be opened")
        exit(1)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_path = sys.argv[1]
        main(arg_path)
    else:
        main()





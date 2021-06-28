#!/usr/bin/env python
# -*- coding: utf-8 -*-
from H1 import draw_graph as dg
from H1 import get_module_usage as gmu
import os
import sys


def main(argument_path=None):
    if argument_path is None:
        _path = os.path.dirname(os.getcwd())
    else:
        _path = argument_path
    try:
        nodes = gmu.main(_path, False, False)
        dg.main(nodes)
    except IOError:
        print("File with path", _path, "could not be opened")
    return 0


if __name__ == '__main__':

    if len(sys.argv) > 1:
        arg_path = sys.argv[1]
        main(arg_path)
    else:
        main()

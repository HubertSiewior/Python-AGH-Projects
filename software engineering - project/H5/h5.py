#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from H1 import get_module_usage as gmu
from H2 import get_function_usage as gfu
from H3 import get_modules_structure as gms
import sys
from H5 import draw_multiple_graphs as dmg

def main(argument_path=None):
    if argument_path is None:
        path = os.path.dirname(os.getcwd())
    else:
        path = os.path.dirname(argument_path)
    try:
        dataH1 = gmu.main(path,False,False)
        dataH2 = gfu.main(path)
        dataH3 = gms.main(path)
        dmg.draw_multiple_graph(dataH1, dataH2, dataH3)
    except IOError:
        print("File with path", argument_path, "could not be opened")



if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_path = sys.argv[1]
        main(arg_path)
    else:
        main()




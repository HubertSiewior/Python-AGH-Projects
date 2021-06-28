#!/usr/bin/env python
# -*- coding: utf-8 -*-
from H4 import export_to_xml as etm
import sys
import os
from H1 import get_module_usage as gmu
from H2 import get_function_usage as gfu
from H3 import get_modules_structure as gms


def main(file_name=None, argument_path=None):
    if argument_path is None:
        _path = os.path.dirname(os.getcwd())
    else:
        _path = argument_path
    try:
        nodesH1 = gmu.main(_path, False, False)
        nodesH2 = gfu.main(_path)
        # nodesH3 = gms.main(_path)
        if file_name is None:
            etm.main("DiagramClassH1", nodesH1, 1)
            etm.main("DiagramClassH2", nodesH2, 2)
            # etm.main("DiagramClassH3", nodesH3, 3)
        else:
            etm.main(file_name + 'H1', nodesH1, 1)
            etm.main(file_name + 'H2', nodesH2, 2)
            # etm.main(file_name + 'H3', nodesH3, 3)
        print("Files have been saved to:", _path)
    except IOError:
        print("File with path", _path, "could not be opened")

    return 0


if __name__ == '__main__':
    if len(sys.argv) > 2:
        arg_path = sys.argv[2]
        file_name = sys.argv[1]
        main(file_name, arg_path)
    else:
        main()

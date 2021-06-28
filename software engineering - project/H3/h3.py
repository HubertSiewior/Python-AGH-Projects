import os
from H3 import get_modules_structure as gms
from H3 import File as F
from H3 import reader as r
from H3 import get_paths as gp
from H3 import  draw_graphH3 as dg



def main():
    ROOT_DIR = os.path.abspath(os.curdir)
    dirs = gp.get_paths(ROOT_DIR)

    modules = gp.get_modules_for_each_path(ROOT_DIR)

    file_table = []

    for path in dirs:
        file = r.parse_file(path)
        file_table.append(F.File(file.name, file.size, file.dependencies, file.functions))

    i = 0
    for file in file_table:
        file.module = modules[i]
        i += 1

    data = gms.get_modules_structure(file_table)
    for directory in data:
        for file in directory:
            print(file)

    dg.draw_graphH3(data)


    return 0


if __name__ == '__main__':
    main()
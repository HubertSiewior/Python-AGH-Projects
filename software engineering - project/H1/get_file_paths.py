#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def get_paths(path):
    paths_array = []
    for file in os.listdir(path):
        if file.endswith(".py"):
            paths_array.append(os.path.join(path, file))

    dir_names_arr = []
    for (dir_path, dir_names, file_names) in os.walk(path):
        dir_names_arr.extend(dir_names)
        break

    for i in range(len(dir_names_arr)):
        paths_from_nested_directories = get_paths(os.path.join(path, dir_names_arr[i]))
        if len(paths_from_nested_directories) > 0:
            paths_array.extend(paths_from_nested_directories)

    all_paths = []
    for _path in paths_array:
        if not _path.endswith("__init__.py") and not os.path.dirname(_path).endswith("tests") and not "venv" in _path and path in _path:
            all_paths.append(_path)
    return all_paths


if __name__ == "__main__":
    print(get_paths(os.path.dirname(os.getcwd())))


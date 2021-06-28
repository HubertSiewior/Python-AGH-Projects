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

    return [path for path in paths_array if not path.endswith("__init__.py") and not os.path.dirname(path).endswith("tests")]


def get_modules_for_each_path(path):

    raw_dirs = os.listdir(path)

    new_paths = []
    for element in raw_dirs:
        if element.startswith('.') or element == 'README.md': continue
        new_paths.append(path + "\\" + str(element))

    dirs = []
    for element in new_paths:
        tmp_arr = os.listdir(element)
        for file in tmp_arr:
            if file == '__init__.py': dirs.append(element)


    return dirs
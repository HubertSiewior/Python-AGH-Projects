import ast
import os
import platform
from H1 import get_file_paths as gfp


def get_function_data(general_path, file_paths):
    data = []
    functions = []
    for file_path in file_paths:
        if platform.system() == 'Windows':
            file_name = file_path.split('\\')[-2:]
        else:
            file_name = file_path.split('/')[-2:]

        for node in ast.walk(ast.parse(open(file_path).read())):
            if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
                name = node.name
                if name is not None and name != "__init__" and name != "__str__" and name != "main":
                    functions.append(name)
                if name == "main":
                    name = file_name[1]+"/"+name
                    functions.append(name)
        data.append([file_name, functions])
        functions = []
    return data


def main(argument_path=None):
    if argument_path is None:
        root_dir = os.path.dirname(os.getcwd())
    else:
        root_dir = argument_path
    dirs = gfp.get_paths(root_dir)
    nodes = get_function_data(root_dir, dirs)
    return nodes

if __name__ == "__main__":
    print(get_function_data(os.path.dirname(os.getcwd()), gfp.get_paths(os.path.dirname(os.getcwd()))))

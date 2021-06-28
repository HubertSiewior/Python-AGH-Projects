import  os
from  modulefinder import ModuleFinder
import importlib
from inspect import getmembers, isfunction, getsource

from H2 import get_function_usage as gfu
from H3 import get_paths as gp
from H3 import Function as F
from H3 import File as file

def get_modules_structure(path):

    directories_array = gp.get_modules_for_each_path(path)
    directories_name = get_directories_name(directories_array)

    modules_structure = [[] for i in range(len(directories_array))]

    directory_files_paths = []
    for element in directories_array:
        directory_files_paths.append(gp.get_paths(element))


    data = get_files_data(path, directory_files_paths[1])

    #for element in data: print(element.get_data())

    for module in data:
        #print(module.get_data())
        print(module.name)
        print(module.size)
        print(module.dependencies)

    return modules_structure

def get_files_data(general_path, file_paths):

    module_finder = ModuleFinder()
    files = []

    for file_path in file_paths:
        spec = importlib.util.spec_from_file_location(file_path, file_path)
        module_from_spec = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module_from_spec)
        functions_list = [function for function in getmembers(module_from_spec) if isfunction(function[1])]
        module = file.Module(file_path.rsplit(os.path.sep, 1)[1].rsplit('.')[0], file_path)
        module.size = os.path.getsize(file_path)
        module_finder.run_script(module.path)
        module.fill_imports_and_functions(general_path, module_finder)
        module.fill_dependecies()
        files.append(module)

        for element in files:
            element.fill_dependecies(files)

    return files

def get_directories_name(directories_array):

    directories_name = []
    for element in directories_array:
        element = element.split('\\')
        directories_name.append(element[len(element) - 1])
    return directories_name

def main(_path):

    data = get_modules_structure(_path)

    return data

if __name__ == '__main__':
    _path = os.path.dirname(os.getcwd())
    modules_structure = main(_path)
    print(modules_structure)

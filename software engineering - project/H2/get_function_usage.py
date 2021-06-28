#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
import os
import importlib.util
from modulefinder import ModuleFinder
from inspect import getmembers, isfunction, getsource
from H1 import get_file_paths as gfp


class Module:
    def __init__(self, _name=None, _path=None):
        self.name = _name
        self.path = _path
        self.imports = []
        self.functions = []

    def fill_imports_and_functions(self, general_path, module_finder):
        module_finder.run_script(self.path)
        for node in ast.walk(ast.parse(open(self.path).read())):
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    self.imports.append([node.module if hasattr(node, "module") else None, alias.name, alias.asname])
            elif isinstance(node, ast.FunctionDef):
                if node.name is not None:
                    self.functions.append(node.name)
        for imported_module in self.imports:
            if len(imported_module) != 4:
                if imported_module[0] is not None and imported_module[1] is not None:
                    name = imported_module[0] + '.' + imported_module[1]
                else:
                    name = imported_module[1]
                for found_module in module_finder.modules.items():
                    if found_module[0] == name:
                        imported_module.append(found_module[1].__file__)
        new_imports = [self.path]
        for imported_module in self.imports:
            if len(imported_module) == 4 and imported_module[3] is not None and general_path in imported_module[3]:
                new_imports.append(imported_module[3])
        self.imports = new_imports


class Function:
    def __init__(self, _name=None, _path=None, _code=None, _module=None):
        self.name = _name
        self.path = _path
        self.code = _code
        self.module = _module
        self.dependencies = []

    def get_data(self):
        return [self.module.name + '.' + self.name, len(self.code), self.dependencies]

    def fill_dependencies(self, _functions):
        for function in _functions:
            used_functions = []
            for node in ast.walk(ast.parse(function.code)):
                if isinstance(node, ast.FunctionDef):
                    used_functions.append(node.name)
            if self == function:
                self.dependencies.append(None)
            elif function.path in self.module.imports:
                count = 0
                for word in self.code.split(" "):
                    if function.name in word:
                        count += 1
                self.dependencies.append(count)
            else:
                self.dependencies.append(0)


def get_function_data(general_path, file_paths):
    module_finder = ModuleFinder()
    functions = []
    for file_path in file_paths:
        spec = importlib.util.spec_from_file_location(file_path, file_path)
        module_from_spec = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module_from_spec)
        functions_list = [function for function in getmembers(module_from_spec) if isfunction(function[1])]
        module = Module(file_path.rsplit(os.path.sep, 1)[1].rsplit('.')[0], file_path)
        module_finder.run_script(module.path)
        module.fill_imports_and_functions(general_path, module_finder)
        for function in functions_list:
            new_function = Function()
            new_function.name = function[1].__name__
            new_function.path = file_path
            new_function.code = getsource(function[1])
            new_function.module = module
            functions.append(new_function)
    for function in functions:
        function.fill_dependencies(functions)
    return functions


def main(path):
    function_data = get_function_data(path, gfp.get_paths(path))
    new_data = []
    for function in function_data:
        new_data.append(function.get_data())
    return new_data


if __name__ == "__main__":
    _path = os.path.dirname(os.getcwd())
    print("Collecting relevant files from " + _path + "...")
    _function_data = main(_path)
    for _function in _function_data:
        print(_function)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ast
from modulefinder import ModuleFinder
from H1 import get_file_paths as gfp


class CallCollector(ast.NodeVisitor):
    def __init__(self):
        self.calls = []
        self.current = None

    def visit_Call(self, _node):
        # FUNCTION OVERLOADING
        self.current = ''
        self.visit(_node.func)
        if self.current is not None:
            self.calls.append(self.current)
        self.current = None

    def generic_visit(self, _node):
        super(CallCollector, self).generic_visit(_node)

    def visit_Name(self, _node):
        # FUNCTION OVERLOADING
        if self.current is not None:
            self.current += _node.id

    def visit_Attribute(self, _node):
        # FUNCTION OVERLOADING
        self.visit(_node.value)
        if self.current is not None:
            self.current += '.' + _node.attr


class FileNode:
    def __init__(self, _name=None, _module_name=None, _size=None,
                 _has_file=None, _path=None, _members=None,
                 _imports=None, _function_calls=None, _dependencies=None):
        self.name = _name
        self.module_name = _module_name
        self.size = _size
        self.has_file = _has_file
        self.path = _path
        self.members = _members
        self.imports = _imports
        self.function_calls = _function_calls
        self.dependencies = _dependencies

    def to_simple_array(self):
        return [self.name, self.size, self.dependencies]

    def to_array(self):
        return [self.name, self.module_name, self.size, self.has_file,
                self.path, self.members, self.imports,
                self.function_calls, self.dependencies]

    def fill_dependencies(self, general_path, module_nodes):
        if self.has_file:
            self.dependencies = []
            try:
                cc = CallCollector()
                cc.visit(ast.parse(open(self.path).read()))
                self.function_calls = list(set(cc.calls))
                for node in module_nodes:
                    imports = []
                    for dependency in self.imports:
                        if len(dependency) == 4:
                            if dependency[3] is not None:
                                if general_path in dependency[3]:
                                    imports.append(dependency[3])
                    if node == self:
                        self.dependencies.append(None)
                    elif node.path in imports:
                        import_index = imports.index(node.path)
                        if self.imports[import_index][0] is not None:
                            if self.imports[import_index][1] == "*":
                                if node.members is not None:
                                    self.dependencies.append(len(node.members))
                                else:
                                    self.dependencies.append(True)
                            else:
                                imports_count = 0
                                for dependency in self.imports:
                                    if dependency[0] == node.module_name:
                                        imports_count += 1
                                self.dependencies.append(imports_count)
                        else:
                            if self.imports[import_index][2] is not None:
                                looking_for = self.imports[import_index][2] + '.'
                            else:
                                looking_for = self.imports[import_index][1] + '.'
                            imports_looking_for = []
                            for function_call in self.function_calls:
                                if looking_for in function_call:
                                    imports_looking_for.append(function_call)
                            imports_looking_for = list(set(imports_looking_for))
                            self.dependencies.append(len(imports_looking_for))
                    else:
                        self.dependencies.append(0)
            except IOError:
                print("Something went wrong while trying to open file", self.path)
                exit(1)

    def fill_imports_and_members(self, module_finder):
        if self.has_file:
            self.imports = []
            self.members = []
            for node in ast.walk(ast.parse(open(self.path).read())):
                if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
                    name = node.name
                    if name is not None:
                        self.members.append(name)
                if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                    for alias in node.names:
                        self.imports.append([node.module if hasattr(node, "module") else None, alias.name, alias.asname])
            self.members = list(set(self.members))
            self.members.sort()
            module_finder.run_script(self.path)
            for module in self.imports:
                if len(module) != 4:
                    if module[0] is not None and module[1] is not None:
                        name = module[0] + '.' + module[1]
                    else:
                        name = module[1]
                    for found_module in module_finder.modules.items():
                        if found_module[0] == name:
                            module.append(found_module[1].__file__)


def get_files_with_modules(directory_path, search_recursively=False):
    files_with_modules = []
    if search_recursively:
        original_file_paths = gfp.get_paths(directory_path)
        unique_file_paths = []
        for file_path_index, file_path in enumerate(original_file_paths):
            files_with_modules.append([file_path, os.path.dirname(file_path).rsplit(os.path.sep, 1)[1]])
        finder = ModuleFinder()
        for file_path in original_file_paths:
            try:
                finder.run_script(file_path)
            except ImportError:
                print("Could not load", file_path)
            for key in finder.modules.items():
                item_path = key[1].__file__ if key[1].__file__ else key[1].__name__ + " (built-in)"
                if '.' not in item_path or item_path.endswith('.py'):
                    item_data = [item_path, key[1].__name__]
                    if item_data[0] not in unique_file_paths and item_data[0] not in original_file_paths:
                        unique_file_paths.append(item_data[0])
                        files_with_modules.append(item_data)
        files_with_modules.sort(key=lambda item: item[0])
    else:
        files_with_modules = gfp.get_paths(directory_path)
        for file_path_index, file_path in enumerate(files_with_modules):
            files_with_modules[file_path_index] = [file_path, os.path.dirname(file_path).rsplit(os.path.sep, 1)[1]]
        files_with_modules.sort(key=lambda item: item[0])
    return files_with_modules


def get_node_data(general_path, file_paths, verbal=False):
    nodes = []
    for file_data in file_paths:
        file_path = file_data[0]
        node = FileNode()
        node.has_file = os.path.isfile(file_path)
        if verbal:
            if node.has_file:
                print("Getting data from file:", file_path)
            else:
                print("Getting data about module without file:", file_path)
        try:
            node.name = file_path.rsplit(os.path.sep, 1)[1] if node.has_file else file_path.rsplit(' ')[0]
            node.module_name = file_data[1]
            node.path = file_path
            if node.name == "__init__.py":
                node.name = file_path.rsplit(os.path.sep, 2)[1]
            node.size = os.path.getsize(file_path) if node.has_file else None
            module_finder = ModuleFinder()
            node.fill_imports_and_members(module_finder)
            nodes.append(node)
        except IOError:
            print("File with path", file_path, "could not be opened, ignoring...")
    if verbal:
        print("Filling node dependencies...")
    for node in nodes:
        node.fill_dependencies(general_path, nodes)
    return nodes


def main(path, deep_search=False, full_info=True, verbal=True):
    nodes = get_node_data(path, get_files_with_modules(path, deep_search), verbal)
    if full_info:
        return [node.to_array() for node in nodes]
    else:
        return [node.to_simple_array() for node in nodes]


if __name__ == "__main__":
    _path = os.path.dirname(os.getcwd())
    print("Collecting relevant files from " + _path + "...")
    data = main(_path, False, True, True)
    for _node in data:
        for index, info in enumerate(_node):
            print(' '*index, info)

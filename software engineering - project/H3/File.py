import ast

class Module:
    def __init__(self, _name=None, _path=None):
        self.name = _name
        self.path = _path
        self.size = None
        self.imports = []
        self.functions = []
        self.dependencies = []

    def get_data(self):
        return [self.name, self.functions, self.imports, self.dependencies]

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

    def fill_dependecies(self, files):

        print(self.name)
        #for file in files:
            #used_functions = []
            #for node in ast.walk(ast.parse())

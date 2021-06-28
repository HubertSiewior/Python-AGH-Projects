import ast

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
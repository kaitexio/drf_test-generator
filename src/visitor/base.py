import ast
import tokenize


class BaseVisitor(ast.NodeVisitor):

    def _read_file(self, filename):
        with tokenize.open(filename) as fd:
            return fd.read()

    def analysis(self, path):
        tree = ast.parse(self._read_file(path))
        self.visit(tree)

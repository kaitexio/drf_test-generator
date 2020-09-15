import os
import tokenize
import ast

from sample.utils import VIEWSET_LIST, TEST_FILE_PATH, VIEW_FILE_PATH, URLS_FILE_PATH


class BaseVisitor(ast.NodeVisitor):

    def _read_file(self, filename):
        with tokenize.open(filename) as fd:
            return fd.read()

    def analysis(self, path):
        """
        渡されたファイルをASTに変換し解析
        """
        tree = ast.parse(self._read_file(path))
        self.visit(tree)

    def exists_path(self, path):
        if os.path.exists(path):
            return True
        return False


class ModelViewSetVisitor(BaseVisitor):

    def __init__(self):
        self.target_class_name = []

    def analysis(self, path):
        super().analysis(path + VIEW_FILE_PATH)
        return self.target_class_name

    def visit_ClassDef(self, node):
        if hasattr(node, "bases") and node.bases:
            for base in node.bases:
                if isinstance(base, ast.Attribute):
                    if base.attr in VIEWSET_LIST:
                        self.target_class_name.append(node.name)
                    # Attributeが入ってくる場合(viewset.ModelViewsetで継承)

                if isinstance(base, ast.Name):
                    if base.id in VIEWSET_LIST:
                        self.target_class_name.append(node.name)
                    # Name(ModelViewsetで継承)


class TestsVisitor(BaseVisitor):
    def __init__(self):
        self.exists = False

    def analysis(self, path):
        super().analysis(path + TEST_FILE_PATH)
        return self.exists

    def visit_ClassDef(self, node):
        self.exists = True


# class UrlsVisitor(BaseVisitor):
#     def __init__(self):
#         self.urls = []
#
#     def analysis(self, path):
#         super().analysis(path + URLS_FILE_PATH)
#         return self.exists

import ast

from src.utils import VIEWSET_LIST, TEST_FILE_PATH, VIEW_FILE_PATH, URLS_FILE_PATH
from src.visitor.base import BaseVisitor


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

                if isinstance(base, ast.Name):
                    if base.id in VIEWSET_LIST:
                        self.target_class_name.append(node.name)


class TestsVisitor(BaseVisitor):
    def __init__(self):
        self.exists = False

    def analysis(self, path):
        super().analysis(path + TEST_FILE_PATH)
        return self.exists

    def visit_ClassDef(self, node):
        self.exists = True


class UrlsVisitor(BaseVisitor):
    def __init__(self):
        self.urls = []

    def analysis(self, path):
        super().analysis(path + URLS_FILE_PATH)
        return self.urls

    def visit_Call(self, node):
        url = self.catch_routed_view(node)
        self.urls.append(url)

    @staticmethod
    def catch_routed_view(node):
        url = {}
        if (func := getattr(node, "func")) and isinstance(func, ast.Attribute):
            if func.value.id == "router" and func.attr == "register":
                for n in node.args:
                    if isinstance(n, ast.Constant):
                        url["Endpoint"] = n.value

                    elif isinstance(n, ast.Name):
                        url["Name"] = n.id

        return url

from src.templates import IMPORT_TEMPLATE, TEMPLATE
from src.writer.base import BaseWriter


class TestWriter(BaseWriter):

    @classmethod
    def write_content(cls, path, *args, **kwargs):
        with open(path, "a")as f:
            if kwargs["is_empty"]:
                cls.write_dependencies(path, IMPORT_TEMPLATE)

            for class_name in kwargs["class_list"]:
                f.write(TEMPLATE % (class_name, class_name))

    @staticmethod
    def write_dependencies(path, content):
        """
        write dependencies packages
        """
        with open(path, "a")as f:
            f.write(content)

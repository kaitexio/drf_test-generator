from sample.templates import IMPORT_TEMPLATE, TEMPLATE
from sample.utils import TEST_FILE_PATH


class BaseWriter(object):
    @classmethod
    def write(cls, path, *args, **kwargs):
        cls.write_content(path + TEST_FILE_PATH, *args, **kwargs)

    @classmethod
    def write_content(cls, path, *args, **kwargs):
        """
        contents of writing files
        """
        raise NotImplementedError('subclasses of BaseWriter must provide an write_content() method')


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

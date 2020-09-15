from src.utils import TEST_FILE_PATH


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

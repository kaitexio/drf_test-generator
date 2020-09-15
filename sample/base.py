from sample.visitor import ModelViewSetVisitor
from sample.writer import TestWriter


class BaseTestGenerator(object):
    writer_class = TestWriter
    visitor_class = ModelViewSetVisitor

    @classmethod
    def generate_test_file(cls, path):
        target_class_name = cls.__get_target_class_list(path)
        cls.__write_test_case(path, target_class_name)

    @classmethod
    def __get_target_class_list(cls, path):
        visitor = cls.get_visitor_class()
        visitor.analysis(path)
        return visitor.target_class_name

    @classmethod
    def __write_test_case(cls, path, class_list):
        writer = cls.get_writer_class()
        writer.write(path, class_list)

    @classmethod
    def get_writer_class(cls):
        assert cls.writer_class is not None, (
                "'%s' should either include a `writer_class` attribute, "
                % cls.__class__.__name__
        )

        return cls.writer_class

    @classmethod
    def get_visitor_class(cls):
        assert cls.visitor_class is not None, (
                "'%s' should either include a `visitor_class` attribute, "
                % cls.__class__.__name__
        )
        return cls.visitor_class()

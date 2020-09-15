import sys

from django.apps import apps, AppConfig
from django.core.management import BaseCommand

from src.visitor.visitor import ModelViewSetVisitor, TestsVisitor, UrlsVisitor
from src.writer.writer import TestWriter


class Command(BaseCommand):
    help = "テストケース自動生成コマンド"

    is_empty = True

    def handle(self, *app_labels, **options):

        has_bad_labels = False
        app_labels = set(app_labels)
        for app_label in app_labels:
            try:
                apps.get_app_config(app_label)
            except LookupError as err:
                self.stderr.write(str(err))
                has_bad_labels = True
        if has_bad_labels:
            sys.exit(2)

        visit_app_path = [config.path for config in apps.get_app_configs() if type(config) is AppConfig]

        for path in visit_app_path:
            test_vi = TestsVisitor()
            exist = test_vi.analysis(path)
            if exist:
                answer = input("%s の中身があるけどいいの？ Please Enter yes or no : " % (path + "/tests.py"))
                if answer in ["no", "n"]:
                    continue

                self.is_empty = False

            visitor = ModelViewSetVisitor()
            class_list = visitor.analysis(path)
            if class_list:
                TestWriter.write(path, class_list=class_list, is_empty=self.is_empty)

            self.stdout.write(".", ending=" ")

        self.stdout.write("\nDone")

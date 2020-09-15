from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='drf-simple-test',  # パッケージ名(プロジェクト名)
    packages=['src'],  # パッケージ内(プロジェクト内)のパッケージ名をリスト形式で指定

    version='0.0.1',  # バージョン

    license='MIT',  # ライセンス

    install_requires=['sqlparse', 'Django', 'asgiref', 'pytz'],  # pip installする際に同時にインストールされるパッケージ名をリスト形式で指定

    author='kaitexio',  # パッケージ作者の名前
    author_email='kaitexio3a05@gmail.com',  # パッケージ作者の連絡先メールアドレス

    url='https://github.com/kaitexio/drf_test-generator',  # パッケージに関連するサイトのURL(GitHubなど)

    description='To generate test class in tests.py.',  # パッケージの簡単な説明
    long_description=long_description,  # PyPIに'Project description'として表示されるパッケージの説明文
    long_description_content_type='text/markdown',
    # long_descriptionの形式を'text/plain', 'text/x-rst', 'text/markdown'のいずれかから指定
    keywords='drf-test django-test',  # PyPIでの検索用キーワードをスペース区切りで指定

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],  # パッケージ(プロジェクト)の分類。https://pypi.org/classifiers/に掲載されているものを指定可能。
)

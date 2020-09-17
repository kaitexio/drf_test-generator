# drf_test_generator

## 内容
Django REST frameworkでのプロジェクト内におけるappのviews.pyを静的解析しModelViewSetを継承しているクラスを検知。
検知したクラス分のCRUDの4パターン分のテストの大枠を自動生成するコマンド

## Installing It

**settings.py**
```
INSTALLED_APPS = (
    ...
    'drf_test_generator',
    ...
)
```

## Using It

```
./manage.py createtestcase
```



## Example

sample/views.py
```python

class SampleViewSet(viewsets.ModelViewSet):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()
    ...

```

sample/tests.py
```python

from rest_framework.test import APITestCase


class SampleViewSetTestCase(APITestCase):
    """このテストはSampleViewSetのテストです"""

    fixtures = []

    def setUp(self):
        pass

    def test_post_case(self):
        url = ''
        data = {}
        self.client.post(url, data, format='json')

    def test_get_case(self):
        url = ''
        self.client.get(url, format='json')

    def test_patch_case(self):
        url = ''
        data = {}
        self.client.patch(url, data={}, format='json')

    def test_delete_case(self):
        url = ''
        data = {}
        self.client.delete(url, data={}, format='json')

```



TEMPLATE = '''\nclass %sTestCase(APITestCase):\n    """このテストは%sのテストです"""\n\n    fixtures = []\n\n    def setUp(self):\n        pass\n\n    def test_post_case(self):\n        url = ''\n        data = {}\n        self.client.post(url, data, format='json')\n\n    def test_get_case(self):\n        url = ''\n        self.client.get(url, format='json')\n\n    def test_patch_case(self):\n        url = ''\n        data = {}\n        self.client.patch(url, data={}, format='json')\n\n    def test_delete_case(self):\n        url = ''\n        data = {}\n        self.client.delete(url, data={}, format='json')\n
'''

IMPORT_TEMPLATE = """from rest_framework.test import APITestCase\n\n"""

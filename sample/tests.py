from rest_framework.test import APITestCase


class ListViewSetTestCase(APITestCase):
    """このテストはListViewSetのテストです"""

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


class PersonViewSetTestCase(APITestCase):
    """このテストはPersonViewSetのテストです"""

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

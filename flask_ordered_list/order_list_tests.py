import order_list
import unittest


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = order_list.app.test_client()

    def test_200_ok(self):
        response = self.app.get('/')
        assert response.status_code == 200

    def simple_list(self):
        return self.app.post('/', data=dict(
            list_to_order='uno\ndue\ntre'
        ))

    def test_simple_list(self):
        response = self.simple_list()
        assert b'due<br>\n        \n        tre<br>\n        \n        uno' in response.data


if __name__ == '__main__':
    unittest.main()

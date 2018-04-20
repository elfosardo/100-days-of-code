import unittest
import unittest.mock as mock
import configparser
from goodreads_tools import *
from goodreads_oauth import *


class TestGoodreads(unittest.TestCase):
    def setUp(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.test_user_id = self.get_test_user_id()

    def get_test_user_id(self):
        test_user_id = self.config['TEST']['user_id']
        return test_user_id

    def test_get_user_shelves(self):
        user_shelves = get_user_shelves(self.test_user_id)
        test_shelves = ['read', 'currently-reading', 'to-read']
        for test_shelf in test_shelves:
            self.assertIn(test_shelf,
                          [shelf['name'] for shelf in user_shelves])

    @staticmethod
    def _mock_requests_response(status=200,
                                content='CONTENT',
                                json_data=None,
                                xml_data=None,
                                raise_for_status=None):
        mock_resp = mock.Mock()
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        mock_resp.status_code = status
        mock_resp.content = content
        if json_data:
            mock_resp.json = mock.Mock(return_value=json_data)
        if xml_data:
            mock_resp.xml = mock.Mock(return_value=xml_data)
        return mock_resp

    @mock.patch('requests.get')
    def test_get_user_shelves_xml(self, mock_get):
        mock_resp = self._mock_requests_response(content='XML_CONTENT')
        mock_get.return_value = mock_resp
        result = get_user_shelves_xml(self.test_user_id)
        self.assertEqual(result, 'XML_CONTENT')

    def test_get_client(self):
        client = get_client()
        self.assertIsNotNone(client)
        self.assertIsInstance(client, oauth2.Client)


if __name__ == '__main__':
    unittest.main()

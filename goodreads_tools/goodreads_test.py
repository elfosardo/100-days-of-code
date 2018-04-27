import unittest
import unittest.mock as mock
import configparser
import config
import oauth2
import requests
import xml

import goodreads_tools as gt
import goodreads_oauth as go


class TestGoodreads(unittest.TestCase):
    def setUp(self):
        self.config = configparser.ConfigParser()
        self.test_user_id = self.get_test_user_id()

    def get_test_user_id(self):
        self.config.read('config.ini')
        test_user_id = self.config['TEST']['user_id']
        return test_user_id

    @staticmethod
    def test_connect_to_site():
        site = config.API_URL
        requests.get(site)

    def test_get_user_shelves(self):
        user_shelves = gt.get_user_shelves(self.test_user_id)
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
        result = gt.get_user_shelves_xml(self.test_user_id)
        self.assertEqual(result, 'XML_CONTENT')

    def test_get_client(self):
        client = go.get_client()
        self.assertIsNotNone(client)
        self.assertIsInstance(client, oauth2.Client)

    def test_get_user_xml(self):
        result = go.get_user_xml()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, xml.dom.minidom.Document)

    @mock.patch('builtins.open', create=True)
    @mock.patch('config.CONFIG_FILE', 'test_config.ini')
    def test_update_config_file(self, mock_open):
        test_values = {
            'test_1': 'one',
            'test_2': 'two'
        }
        go.update_config_file('TEST', test_values, config.CONFIG_FILE)
        self.assertEqual(config.config['TEST']['test_1'], 'one')
        self.assertEqual(config.config['TEST']['test_2'], 'two')


if __name__ == '__main__':
    unittest.main()

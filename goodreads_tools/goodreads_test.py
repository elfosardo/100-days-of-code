import unittest
import configparser
from goodreads_tools import get_user_shelves


class TestGoodreads(unittest.TestCase):
    def setUp(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def test_get_user_shelves(self):
        user_id = self.config['TEST']['user_id']
        user_shelves = get_user_shelves(user_id)
        test_shelves = ['read', 'currently-reading', 'to-read']
        for test_shelf in test_shelves:
            self.assertIn(test_shelf,
                          [shelf['name'] for shelf in user_shelves])


if __name__ == '__main__':
    unittest.main()

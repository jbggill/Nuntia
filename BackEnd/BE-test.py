import unittest
from app import app
import os


class AppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_handle_post_with_html(self):
        # Test the POST request with HTML content
        dir_path = os.path.dirname(os.path.realpath(__file__))  # get the directory of current script
        with open(os.path.join(dir_path, 'example_article.txt'),'r') as txt:  # use the directory path to construct full path to the file
            html = txt.read()
        data = {'html': html}
        response = self.app.post('/', json=data)
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)
        self.assertIsInstance(data['message'], dict)

    def test_handle_post_with_url(self):
        # Test the POST request with URL
        data = {'url': 'https://edition.cnn.com/europe/live-news/russia-ukraine-war-news-07-14-23/index.html'}
        response = self.app.post('/', json=data)
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)
        self.assertIsInstance(data['message'], dict)

    def test_handle_post_insufficient_information(self):
        # Test the POST request with insufficient information
        data = {}
        response = self.app.post('/', json=data)
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()

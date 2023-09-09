import unittest

from api_requests.simple_books_requests import SimpleBooksRequests


class TestGetStatus(unittest.TestCase):
    """
    Testam ruta /status
    """

    def setUp(self):
        self.requests_handler = SimpleBooksRequests()

    def test_get_status(self):
        """
        Verificam:

        status code-ul este 200
        in response, avem cheia status cu valoarea OK """

        response = self.requests_handler.get_status()
        expected_status_code = 200
        expected_api_status = "OK"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_api_status, response.json()["status"])
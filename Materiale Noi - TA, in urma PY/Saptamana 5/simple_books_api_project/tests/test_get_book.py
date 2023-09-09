import unittest

from api_requests.simple_books_requests import SimpleBooksRequests


class TestGetBook(unittest.TestCase):
    """
    Testam ruta GET /books/<book_id>
    """

    def setUp(self):
        self.requests_handler = SimpleBooksRequests()

    def test_get_book_by_id_when_exists_in_db(self):
        """
        Verificam:

        status code-ul este 200
        in response am obtinut cartea cu id-ul dorit"""

        book_id = 1
        response = self.requests_handler.get_book_by_id(book_id=book_id)
        expected_status_code = 200
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(book_id, response.json()["id"])

    def test_get_book_by_id_when_does_not_exists_in_db(self):
        """
        Verificam:

        status code-ul este 404
        in response am obtinut eroarea asteptata"""

        book_id = 200
        response = self.requests_handler.get_book_by_id(book_id=book_id)
        expected_status_code = 404
        expected_error = f"No book with id {book_id}"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_error, response.json()["error"])

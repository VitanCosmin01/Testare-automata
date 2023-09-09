import unittest

from api_requests.simple_books_requests import SimpleBooksRequests


class TestSubmitOrder(unittest.TestCase):
    """
    Testam ruta POST/orders
    Authetication required
    Exemple of request body:
            {
                "bookId": 1,
                "customerName": "Laurentia"
            }
    """

    def setUp(self) -> None:
        self.request_handler = SimpleBooksRequests()

    def test_order_an_available_book(self):
        """
        Verificam:

        status code este 201
        status-ul comenzii create este "true"
        avem cheia orderId in response"""


        response = self.request_handler.submit_order(book_id=1, customer_name='Laurentia')
        expected_status_code = 201
        expected_status_order = True
        expected_key = "orderId"
        key_list = response.json().keys()
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_status_order, response.json()['created'])
        self.assertIn(expected_key, key_list)


    def test_order_unavailable_book(self):
        """
        Verificam:

        status code este 404
        mesajul de eroare este cel asteptat"""


        response = self.request_handler.submit_order(book_id=2, customer_name='Laurentia')
        expected_status_code = 404
        expected_error_msg = "This book is not in stock. Try again later."
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_error_msg, response.json()['error'])


    def test_order_book_which_is_not_in_db(self):
        """
        Verificam:

        status code este 400
        mesajul de eroare este cel asteptat"""


        response = self.request_handler.submit_order(book_id=100, customer_name='Laurentia')
        expected_status_code = 400
        expected_error_msg = "Invalid or missing bookId."
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_error_msg, response.json()['error'])
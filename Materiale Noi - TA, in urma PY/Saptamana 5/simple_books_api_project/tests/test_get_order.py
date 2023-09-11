import unittest

from api_requests.simple_books_requests import SimpleBooksRequests

class TestGetOrder(unittest.TestCase):

    """
    Testam ruta GET / order
    Authentication required

    """
    def setUp(self) -> None:
        self.requests_handler = SimpleBooksRequests()

    def test_get_order_when_order_is_in_db(self):
        """
        Verificam:

        status code este 200-"""

        submit_response = self.requests_handler.submit_order(book_id=1, customer_name="Vitan")  # am apelat metoda -submit_order- pt a avea o comanda creata
        order_id = submit_response.json()["orderId"]
        response = self.requests_handler.get_order_by_id(order_id=order_id)
        expected_status_code = 200
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(order_id, response.json()["id"])

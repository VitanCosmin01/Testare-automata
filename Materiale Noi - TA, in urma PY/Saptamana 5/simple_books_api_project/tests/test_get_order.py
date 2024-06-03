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

    def test_get_order_when_order_is_not_in_db(self):
        """
        Verificam:

        - status code este 404
        - verificam eroarea aparuta "No order with id aaaaaaaaaaaaaaaaaa."
        """
        order_id = "aaaaaaaaaaaaaaaaaa"
        response = self.requests_handler.get_order_by_id(order_id=order_id)
        expected_status_code = 404
        actual_status_code = response.status_code
        expected_error = f"No order with id {order_id}."
        actual_error = response.json()["error"]
        self.assertEqual(expected_status_code, actual_status_code)
        self.assertEqual(expected_error, actual_error)

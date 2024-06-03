import unittest

from api_requests.simple_books_requests import SimpleBooksRequests


class TestDeleteOrder(unittest.TestCase):
    """
    Testam ruta DELETE /orders/<order_id>
    Requires authentication
    """

    def setUp(self):
        self.request_handler = SimpleBooksRequests()

    def test_delete_order_wich_exist_in_db(self):
        order_id = self.request_handler.submit_order(book_id=1, customer_name="Vitan")
        response = self.request_handler.delete_order(order_id=order_id)
        expected_status_code = 404
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code, actual_status_code)

    def test_delete_order_wich_doesnt_exist_in_db(self):
        order_id = 300000
        response = self.request_handler.delete_order(order_id=order_id)
        expected_status_code = 404
        actual_status_code = response.status_code
        expected_error = f"No order with id {order_id}."
        actual_error = response.json()["error"]
        self.assertEqual(expected_status_code, actual_status_code)
        self.assertEqual(expected_error, actual_error)

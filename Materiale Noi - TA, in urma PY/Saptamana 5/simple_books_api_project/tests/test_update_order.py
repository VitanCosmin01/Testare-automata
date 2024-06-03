import unittest

from api_requests.simple_books_requests import SimpleBooksRequests


class TestUpdateOrder(unittest.TestCase):
    """
    Testam ruta PATCH orders/<orderId>
    Authetication required
    Exemple of request body:
        {
            "customerName": "Viorel"
        }
    """

    def setUp(self):
        self.request_handler = SimpleBooksRequests()

    def test_update_an_order_that_exist_in_db(self):
        """
        - verificam ca status code este 204
        - verificam ca s-a modificat customerName in Viorel
        """

        order = self.request_handler.submit_order(book_id=1, customer_name="Vitan")
        order_id = order.json()["orderId"]
        print(order_id)
        response = self.request_handler.update_order(order_id=order_id, customer_name="Viorel")
        print(response)
        expected_status_code = 204
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code, actual_status_code)

import unittest

from api_requests.simple_books_requests import SimpleBooksRequests


class TestGetOrders(unittest.TestCase):

    """
    testam ruta GET /orders

    """

    def setUp(self) -> None:
        self.requests_handler = SimpleBooksRequests()

    def test_get_all_orders(self):
        """
        verificam:
        -status code este 200
        -primim exact cate comenzi exista in DB

        """
        # self.requests_handler.submit_order(book_id=1, customer_name="Vitan")      # aici s-au creat 2 comenzi
        # self.requests_handler.submit_order(book_id=1, customer_name="Vitan")
        response = self.requests_handler.get_all_books()
        expected_status_code = 200
        expected_all_orders = 6   # in Postman avem 3 comenzi dar in Pycharm ne da 6! De ce? din cauza comenzilor create pe tokenul respectiv .
        # in Pycharm am definit constructorul __init__ din SimpleBooksRequests prin care se genereaza cate un token de fiecare data cand apelam metoda
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_all_orders, len(response.json()))



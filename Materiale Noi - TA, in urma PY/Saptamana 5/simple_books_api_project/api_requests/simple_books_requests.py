import requests
import random


class SimpleBooksRequests:
    _BASE_URL = "http://simple-books-api.glitch.me"

    def __init__(self):
        self.token = self._generate_token()

    def _generate_token(self):
        url = f"{self._BASE_URL}/api-clients"
        random_number = random.randint(1, 9999999999999999999)
        request_body = {
            "clientName": "PYTA05",
            "clientEmail": f"pyta05{random_number}@gmail.com"
        }
        resp = requests.post(url=url, json=request_body)
        return resp.json()["accessToken"]

    def get_status(self):
        url = f"{self._BASE_URL}/status"
        resp = requests.get(url=url)
        return resp

    def get_all_books(self, limit=None, type=None):
        url = f"{self._BASE_URL}/books"
        if limit is not None and type is not None:
            ...
        elif limit is not None and type is not None:
            url += f"?limit={limit}"
        elif type is not None:
            url += f"?type={type}"

        request_params = {}
        if limit is not None:
            request_params.update({"limit": limit})
        if type is not None:
            request_params.update({"type": type})

        resp = requests.get(url=url,  params=request_params)
        return resp

    def get_book_by_id(self, book_id):
        url = f"{self._BASE_URL}/books/{book_id}"
        resp = requests.get(url=url)
        return resp

    def submit_order(self, book_id, customer_name):
        url = f"{self._BASE_URL}/orders"
        request_body = {
            "bookId": book_id,
            "customerName": customer_name
        }
        resp = requests.post(url=url, json=request_body, headers={"authorization": self.token})
        return resp

    def get_all_orders(self):
        url = url = f"{self._BASE_URL}/orders"
        resp = requests.get(url=url, headers={"Authorization": self.token})
        return resp

    def get_order_by_id(self, order_id):
        url = f"{self._BASE_URL}/orders/{order_id}"
        resp = requests.get(url=url, headers={"Authorization": self.token})
        return resp

    def update_order(self, order_id, customer_name):
        url = f"{self._BASE_URL}/orders/{order_id}"
        request_body = {
            "customerName": customer_name
        }
        resp = requests.patch(url=url, json=request_body, headers={"Authorization": self.token})
        return resp

    def delete_order(self, order_id):
        url = f"{self._BASE_URL}/orders/{order_id}"
        resp = requests.delete(url=url, headers={"Authorization": self.token})
        return resp

# get status


# obj1 = SimpleBooksRequests()
# response = obj1.get_status()
# print(response.status_code)
# print(response.json())
#
# #  get all books
# response2 = obj1.get_all_books()
# obj1.get_all_books(limit=4)
# obj1.get_all_books(type="fiction")
# obj1.get_all_books(limit=5, type="non-fiction")
# print(response2.status_code)
# print(response2.json())

# resp3 = obj1.submit_order(3, "Cosmina")
# print(resp3.status_code)
# print(resp3.json())

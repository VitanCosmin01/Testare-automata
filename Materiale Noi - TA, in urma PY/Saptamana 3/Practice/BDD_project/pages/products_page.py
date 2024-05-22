import time

from selenium.webdriver.common.by import By

from base_page import BasePage


class ProductPage(BasePage):
    username_el = (By.ID, "user-name")
    password_el = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"

    def navigate_to_product_page(self):
        self.browser.get(self.BASE_URL)
        user = self.browser.find_element(*self.username_el)
        user.send_keys(self.USERNAME)
        time.sleep(3)
        password = self.browser.find_element(*self.password_el)
        password.send_keys(self.PASSWORD)
        time.sleep(3)
        button = self.browser.find_element(*self.LOGIN_BTN)
        button.click()
        time.sleep(5)
        expected_url = "https://www.saucedemo.com/inventory.html"
        actual_url = self.browser.current_url
        assert expected_url == actual_url

    def click_name(self):
        first_title_elem = self.browser.find_element(By.ID, "item_4_title_link")
        first_title_elem.click()

    def product_detail_page(self):
        expected_url = "https://www.saucedemo.com/inventory-item.html?id=4"
        actual_url = self.browser.current_url
        assert expected_url == actual_url

    def click_picture(self):
        first_picture_elem = self.browser.find_element(By.ID, "item_4_img_link")
        first_picture_elem.click()

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()

    def check_kart(self):
        actual_kart = self.browser.find_element(By.ID, "shopping_cart_container").text
        expected_kart_item = str(1)
        assert actual_kart == expected_kart_item

    def remove_from_kart(self):
        remove_to_cart_button = self.browser.find_element(By.ID, "remove-sauce-labs-backpack")
        remove_to_cart_button.click()

    def check_empty_kart(self):
        actual_kart = self.browser.find_element(By.CLASS_NAME, "shopping_cart_link").text
        expected_kart_item = ""
        assert actual_kart == expected_kart_item




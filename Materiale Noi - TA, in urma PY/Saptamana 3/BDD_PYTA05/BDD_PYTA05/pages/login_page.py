from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.TAG_NAME, "h3")

    def navigate_to_login_page(self):
        self.browser.get(self.BASE_URL)

    def insert_correct_username(self):
        username = self.browser.find_element(*self.USERNAME)
        username.send_keys("standard_user")

    def insert_correct_password(self):
        password = self.browser.find_element(*self.PASSWORD)
        password.send_keys("secret_sauce")

    def insert_incorrect_password(self):
        password = self.browser.find_element(*self.PASSWORD)
        password.send_keys("incorrect_password")

    def click_login_button(self):
        login_btn = self.browser.find_element(*self.LOGIN_BTN)
        login_btn.click()

    def check_error_message_invalid_pwd(self):
        expected_error = "Epic sadface: Username and password do not match any user in this service"
        error_element = self.browser.find_element(*self.ERROR_MSG)
        actual_error = error_element.text
        assert expected_error == actual_error

    # scenario 3
    def insert_incorrect_username(self):
        username = self.browser.find_element(*self.USERNAME)
        username.send_keys("incorrect_user")

    # Scenario 3

    def check_error_message_invalid_username(self):
        expected_error = "Epic sadface: Username and password do not match any user in this service"
        error_element = self.browser.find_element(*self.ERROR_MSG)
        actual_error = error_element.text
        assert expected_error == actual_error

    # Scenario 4

    def check_error_message_password_required(self):
        expected_error = "Epic sadface: Password is required"
        error_element = self.browser.find_element(*self.ERROR_MSG)
        actual_error = error_element.text
        assert expected_error == actual_error

    # Scenario 5
    def check_error_message_username_required(self):
        expected_error = "Epic sadface: Username is required"
        error_element = self.browser.find_element(*self.ERROR_MSG)
        actual_error = error_element.text
        assert expected_error == actual_error

    # Scenario 6
    # Pentru scenariul 6 avem definite functiile deja

    # Scenario 7
    # Pentru scenariul 7 avem definite functiile deja

    # Scenario 8
    # Pentru scenariul 8 avem definite functiile deja

    # Scenario 9
    # Pentru scenariul 9 avem definite functiile deja

    # Scenario 10
    def insert_locked_username(self):
        locked_username = self.browser.find_element(*self.USERNAME)
        locked_username.send_keys("locked_out_user")

    def check_error_message_locked_username(self):
        expected_error = "Epic sadface: Sorry, this user has been locked out."
        error_element = self.browser.find_element(*self.ERROR_MSG)
        actual_element = error_element.text
        assert expected_error == actual_element

from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG_INVALID_PWD = (By.TAG_NAME, "h3")

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
        error_element = self.browser.find_element(*self.ERROR_MSG_INVALID_PWD)
        actual_error = error_element.text
        assert expected_error == actual_error

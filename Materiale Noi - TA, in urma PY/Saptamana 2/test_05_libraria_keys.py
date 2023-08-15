"""
LIBRARIA keys

- import necesar: from selenium.webdriver import Keys

- Folosind clasa Keys din libraria keys, putem sa introducem o
simulare a tastelor direct prin intermediul automatizarii.
"""
import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestKeys(unittest.TestCase):

    USERNAME = (By.ID, "username")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.implicitly_wait(1)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_keys(self):
        user = self.driver.find_element(*self.USERNAME)
        user.send_keys("tmsmith")
        time.sleep(3)
        user.clear()
        user.send_keys("tmsmith")
        time.sleep(3)
        user.send_keys(Keys.CONTROL, 'a')
        time.sleep(3)
        user.send_keys(Keys.BACKSPACE)
        time.sleep(3)
        user.send_keys("tmsmith")
        time.sleep(3)
        user.send_keys(Keys.BACKSPACE)
        time.sleep(3)
        user.send_keys(Keys.ARROW_LEFT)
        time.sleep(3)
        user.send_keys(Keys.ARROW_LEFT)
        time.sleep(3)
        user.send_keys(Keys.ARROW_LEFT)
        time.sleep(2)

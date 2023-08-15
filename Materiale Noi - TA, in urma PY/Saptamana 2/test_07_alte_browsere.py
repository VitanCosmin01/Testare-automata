"""
Chrome vs Firefox vs Edge
"""

import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class TestDifferentBrowsers(unittest.TestCase):

    LINK = "https://formy-project.herokuapp.com/form"

    def test_chrome(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        # driver = webdriver.Chrome()
        driver.get(self.LINK)
        expected_url = "https://formy-project.herokuapp.com/form"
        actual_url = driver.current_url
        time.sleep(1)
        self.assertEqual(expected_url, actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}")
        driver.quit()

    def test_firefox(self):
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        # driver = webdriver.Firefox()
        driver.get(self.LINK)
        expected_url = "https://formy-project.herokuapp.com/form"
        actual_url = driver.current_url
        time.sleep(1)
        self.assertEqual(expected_url, actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}")
        driver.quit()

    def test_edge(self):
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        # driver = webdriver.Edge()
        driver.get(self.LINK)
        expected_url = "https://formy-project.herokuapp.com/form"
        actual_url = driver.current_url
        time.sleep(1)
        self.assertEqual(expected_url, actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}")
        driver.quit()

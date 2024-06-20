import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestYoutubePage(unittest.TestCase):
    LINK = "https://www.youtube.com/"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.implicitly_wait(10)
        # accept cookies
        accept_cookies = self.driver.find_element(By.XPATH,
                                                  "//*[@id='content']/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
        accept_cookies.click()
    def tearDown(self):
        self.driver.close()

    def test_login(self):
        pass



if __name__ == '__main__':
    unittest.main()

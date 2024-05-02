"""
Folosind libraria unittest, testeaza pagina de login
de pe site-ul https://the-internet.herokuapp.com/login
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginPage(unittest.TestCase):
    LINK = "https://the-internet.herokuapp.com/login"
    BTN_LOGIN = (By.XPATH, "//button[@class='radius']")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    ERROR_MSG = (By.ID, "flash")

    def setUp(self):
        """
        Definim instructiunile pe care dorim sa le efectuam
        inainte de fiecare test.
        Aceasta metoda se va apela de fiecare data inainte de rularea
        unui test
        """
        print("INAINTE DE RULARE TEST")
        # instantierea driver-ului
        self.driver = webdriver.Chrome()

        # accesarea paginii pe care dorim sa o testam
        self.driver.get(self.LINK)

        # maximizarea ferestrei de browser
        self.driver.maximize_window()

    def tearDown(self):
        """
        Definim instructiunile pe care dorim sa le efectuam
        dupa rularea fiecarui test.
        Aceasta metoda se va apela de fiecare data dupa rularea
        unui test
        """
        print("DUPA RULARE TEST")
        # inchidem driver-ul
        self.driver.quit()

    # TEST 1:
    # - Verifica URL-ul paginii curente este corect
    #@unittest.skip
    def test_current_url(self):
        print("RULARE TEST")
        actual_url = self.driver.current_url
        expected_url = self.LINK

        # assert actual_url == expected_url
        self.assertEqual(actual_url, expected_url, "Unexpected URL")

    # TEST 2:
    # - Verifica ca titlul paginii apare corect
    #@unittest.skip
    def test_title_page(self):
        pass

    # TEST 3:
    # - Verifica daca textul de pe elementul h2 este corect

    def test_h2_text(self):
        h2_element = self.driver.find_element(By.TAG_NAME, "h2")
        actual_text = "Login Page"
        expected_text = h2_element.text
        self.assertEqual(actual_text, expected_text, "Unexpected text")

    # TEST 4:
    # - Verifica ca butonul de Login este displayed/apare pe site
    def test_btn_login_is_displayed(self):
        btn_login_el = self.driver.find_element(*self.BTN_LOGIN)
        # # *args si **kwargs
        # self.driver.find_element((By.XPATH, "..."))
        # self.driver.find_element(By.XPATH, "...")
        self.assertTrue(btn_login_el.is_displayed(), "Butonul de Login nu este afisat")

    # TEST 5:
    # - username incorect + parola corecta
    def test_login_when_username_is_incorrect(self):
        # introducem un username incorect
        username_element = self.driver.find_element(*self.USERNAME)
        username_element.send_keys("Cosmina")

        # introducem o parola corecta
        password_element = self.driver.find_element(*self.PASSWORD)
        password_element.send_keys("SuperSecretPassword!")

        # sa incercam sa ne logam
        btn_login = self.driver.find_element(*self.BTN_LOGIN)
        btn_login.click()

        # verificam ca avem mesajul de eroare asteptat
        error_msg_element = self.driver.find_element(*self.ERROR_MSG)
        actual_error = error_msg_element.text
        print("============================")
        print(actual_error)
        self.assertIn("Your username is invalid!", actual_error)

    # TEST 6:
    # - username corect + parola incorecta
    def test_login_when_password_is_incorrect(self):
        username_element = self.driver.find_element(*self.USERNAME)
        username_element.send_keys("tomsmith")
        password_element = self.driver.find_element(*self.PASSWORD)
        password_element.send_keys("123")
        btn_login = self.driver.find_element(*self.BTN_LOGIN)
        btn_login.click()
        error_msg_element = self.driver.find_element(*self.ERROR_MSG)
        actual_error = error_msg_element.text
        self.assertIn("Your password is invalid!", actual_error)

    # TEST 7:
    # - username corect + parola corecta
    #@unittest.skip
    def test_login_when_all_are_correct(self):
        username_element = self.driver.find_element(*self.USERNAME)
        username_element.send_keys("tomsmith")
        password_element = self.driver.find_element(*self.PASSWORD)
        password_element.send_keys("SuperSecretPassword!")
        btn_login = self.driver.find_element(*self.BTN_LOGIN)
        btn_login.click()
        succes_msg_element = self.driver.find_element(*self.ERROR_MSG)
        actual_succes_msg = succes_msg_element.text
        self.assertIn("You logged into a secure area!", actual_succes_msg)

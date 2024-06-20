"""
1. Intrati pe site-ul https://www.elefant.ro/
"""
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# service = Service(ChromeDriverManager().install())


class TestElefant(unittest.TestCase):
    LINK = "https://www.elefant.ro/"
    SEARCH_BAR = (By.XPATH, "//*[@name='SearchTerm']")
    COOKIES_SITE = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    SEARCH_BTN = (By.XPATH, '//*[@id="HeaderRow"]/div[4]/div/div[1]/form/button')
    PROD_LIST = (By.CLASS_NAME, 'product-title')
    CONT_BUTN_ELEMENT = (By.XPATH, "//*[@id='HeaderRow']/div[4]/div/ul/li[1]/a[1]/div")
    CONECTARE_ELEMENT = (By.XPATH, "//*[@id='account-layer']/a[1]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='ShopLoginForm_Login']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='ShopLoginForm_Password']")
    SUBMIT_BTTN = (By.XPATH, "//div[@class='col-sm-12']/button")
    ALERT_ERROR_MSG = (By.XPATH, "//div[@class='alert alert-danger']")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.implicitly_wait(10)

        # Accept cookies
        cookies_btn = self.driver.find_element(*self.COOKIES_SITE)
        cookies_btn.click()

    def tearDown(self):
        self.driver.quit()

    # @unittest.skip
    def test_search_results_list(self):
        """
        2. - Cautam un produs la alegere (iphone 14)
        - Verificam ca s-au returnat
        cel putin 10 rezultate ([class="product-title"])
        """
        time.sleep(4)
        search_bar = self.driver.find_element(*self.SEARCH_BAR)
        search_bar.send_keys("Iphone 14")
        time.sleep(4)

        search_btn = self.driver.find_element(*self.SEARCH_BTN)
        search_btn.click()
        time.sleep(4)

        product_list = self.driver.find_elements(*self.PROD_LIST)
        self.assertLessEqual(len(product_list), 10)
        time.sleep(3)
        print(product_list)

        """
        3. Extrageti din lista produsul cu pretul cel mai mic [class="current-price "]
        din primele 10 produse gasite
        (puteti sa va folositi de find_elements)
        """
    # @unittest.skip
    def test_find_lower_price(self):
        # identificam search bar si introducem cuvantul de cautare
        search_bar = self.driver.find_element(*self.SEARCH_BAR)
        search_bar.send_keys("Iphone 14")
        time.sleep(4)
        # identificam butonul de cautare si dam click
        search_btn = self.driver.find_element(*self.SEARCH_BTN)
        self.driver.execute_script("arguments[0].click();", search_btn)
        # search_btn.click()
        time.sleep(4)
        # identificam elementul care corespunde pretului
        price_elements = self.driver.find_elements(By.CLASS_NAME, "current-price")  #  se foloseste daca apar ferestre pop-up in loc la  .click
        print(price_elements)
        prices = []
        # iteram prin lista de preturi pentru a inlocui punctul cu virgula si updatam lista de preturi
        for price_element in price_elements[:11]:
            price_list = price_element.text.split()
            print(price_list)
            price = float(price_list[0].replace(".", "").replace(",", "."))
            print(price)
            prices.append(price)
        print(prices)
        """
        4. Extrageti titlul paginii si verificati ca este corect
        """
    # @unittest.skip
    def test_pagetitle(self):
        actual_title = self.driver.title
        expected_title = ("elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste "
                          "500.000 de produse pentru tine!")
        self.assertEqual(actual_title, expected_title, "Titlul este corect!")


    """
    5. Intrati pe site, accesati butonul cont si click pe conectare.
    Identificati elementele de tip user si parola si inserati valori incorecte
    (valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid)
    - Dati click pe butonul "conectare" si verificati urmatoarele:
                1. Faptul ca nu s-a facut logarea in cont
                2. Faptul ca se returneaza eroarea corecta
    """
    def test_login_with_wrong_credentials(self):
        cont_button_element = self.driver.find_element(*self.CONT_BUTN_ELEMENT)
        cont_button_element.click()
        conectare_element = self.driver.find_element(*self.CONECTARE_ELEMENT)
        conectare_element.click()
        email_input = self.driver.find_element(*self.EMAIL_INPUT)
        email_input.send_keys("vitan.cosmin83@gmail.com")
        time.sleep(4)
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys("123456789")
        time.sleep(4)
        submit_button = self.driver.find_element(*self.SUBMIT_BTTN)
        submit_button.click()
        time.sleep(5)
        # 1
        actual_title = self.driver.title
        expected_title = "Conectare"
        self.assertEqual(actual_title, expected_title, "diferite")
        # 2
        alert_error_msg = self.driver.find_element(*self.ALERT_ERROR_MSG).text
        expected_error_msg = "Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou."
        # assert alert_error_msg == expected_error_msg
        self.assertEqual(alert_error_msg, expected_error_msg, "diferite")
    """
    6. Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@")
    si verificati faptul ca butonul "conectare" este dezactivat
    """
    def test_deactivated_conection_button(self):
        cont_button_element = self.driver.find_element(*self.CONT_BUTN_ELEMENT)
        cont_button_element.click()
        conectare_element = self.driver.find_element(*self.CONECTARE_ELEMENT)
        conectare_element.click()
        time.sleep(3)
        email_input = self.driver.find_element(*self.EMAIL_INPUT)
        time.sleep(3)
        email_input.clear()
        time.sleep(3)
        email_input.send_keys("vitan.cosmin")
        freezed_buton = self.driver.find_element(By.CLASS_NAME, "btn-block")
        self.assertTrue(freezed_buton)

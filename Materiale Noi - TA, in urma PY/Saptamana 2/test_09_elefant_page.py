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

    def test_search_results_list(self):
        """
        2. - Cautam un produs la alegere (iphone 14)
        - Verificam ca s-au returnat
        cel putin 10 rezultate ([class="product-title"])
        """
        time.sleep(4)
        search_bar = self.driver.find_element(*self.SEARCH_BAR)
        search_bar.send_keys("Iphone 14")

        search_btn = self.driver.find_element(*self.SEARCH_BTN)
        search_btn.click()

        product_list = self.driver.find_elements(*self.PROD_LIST)
        self.assertGreaterEqual(len(product_list), 10)
        time.sleep(3)


"""
3. Extrageti din lista produsul cu pretul cel mai mic [class="current-price "]
din primele 10 produse gasite
(puteti sa va folositi de find_elements)
"""

"""
4. Extrageti titlul paginii si verificati ca este corect
"""

"""
5. Intrati pe site, accesati butonul cont si click pe conectare.
Identificati elementele de tip user si parola si inserati valori incorecte
(valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid)
- Dati click pe butonul "conectare" si verificati urmatoarele:
             1. Faptul ca nu s-a facut logarea in cont
            2. Faptul ca se returneaza eroarea corecta
"""

"""
6. Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@")
si verificati faptul ca butonul "conectare" este dezactivat
"""

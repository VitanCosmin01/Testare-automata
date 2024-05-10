"""
EXERCITIU:

Acceseaza pagina https://www.ebay.com/.

Interactioneaza cu dropdown-ul de categorii de pe pagina principala,
si selecteaza o optiune disponibila.

a. selectare dupa text
b. selectare dupa value
c. selectare dupa index
"""

# executam importurile
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

# instantiem driver-ul
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()

# salvam linkul intr-o constanta
LINK = "https://www.ebay.com/"

# accesam link-ul
driver.get(LINK)
# maximizam fereastra
driver.maximize_window()
time.sleep(4)

# interactiune dropdown
select_object = Select(driver.find_element(By.ID, "gh-cat"))
# print(select_object.options)

# selectare dupa text
# select_object.select_by_visible_text("Antiques")
# time.sleep(4)

# selectare dupa value
# select_object.select_by_value("20081")  # ->Antiques
# time.sleep(4)

# selectare dupa index
select_object.select_by_index(1)   # ->Antiques
time.sleep(4)

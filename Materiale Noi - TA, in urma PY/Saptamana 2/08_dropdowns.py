"""
Interactiunea cu DROPDOWN-URI

LINK: https://the-internet.herokuapp.com/dropdown
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.select import Select

LINK = "https://the-internet.herokuapp.com/dropdown"

# instantiem driver-ul
# service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()

# accesam link-ul
driver.get(LINK)

# maximizam fereastra
driver.maximize_window()

# interactiune dropdown

# select_object = Select(driver.find_element(By.ID, "dropdown"))
# print(select_object.options)
#
# for option in select_object.options:
#     print(option.text)
#     if option.text == "Please select an option":
#         assert not option.is_enabled()

# # selectare optiune dupa text -> select_by_visibile_text
# select_object.select_by_visible_text("Option 1")
# time.sleep(4)
#
# # selectare optiune dupa value -> select_by_value
# select_object.select_by_value("1")
# time.sleep(4)
#
# # selectare optiune dupa index -> select_by_index
# select_object.select_by_index(1)
# time.sleep(5)

"""
EXERCITIU:

Acceseaza pagina https://www.ebay.com/.

Interactioneaza cu dropdown-ul de categorii de pe pagina principala,
si selecteaza o optiune disponibila.

a. selectare dupa text
b. selectare dupa value
c. selectare dupa index
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

LINK = "https://www.ebay.com/"
# instantiem driver-ul
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()
# maximizam fereastra
driver.get(LINK)
driver.maximize_window()
# identificare element dupa ID
select_object = Select(driver.find_element(By.ID, 'gh-cat'))
# a. selectare dupa text
select_object.select_by_visible_text("Books")
time.sleep(2)
# b. selectare dupa value
select_object.select_by_value('267')
time.sleep(2)
# c. selectare dupa index
select_object.select_by_index(3)
time.sleep(2)

cookies = driver.find_element(By.ID, "gdpr-banner-accept")
cookies.click()
time.sleep(3)

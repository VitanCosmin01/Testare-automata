# selenium si webdriver-manager -> librarii ce trebuie instalate
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# varianta simpla de instantiere browser
driver = webdriver.Chrome()

# varianta mai complicata dar mai avantajoasa
# deoarece nu mai depindem daca browser-ul este instalat
# sau nu pe calculator -> varianta RECOMANDATA
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# accesam un link
LINK = "https://formy-project.herokuapp.com/"
driver.get(LINK)
time.sleep(3)

# maximizam fereastra
driver.maximize_window()
time.sleep(3)


# Vrem sa accesam link-ul Autocomplete de pe pagina web
autocomplete_link = driver.find_element(By.LINK_TEXT, "Autocomplete")
autocomplete_link.click()
time.sleep(3)


# navigam inapoi
driver.back()
time.sleep(2)

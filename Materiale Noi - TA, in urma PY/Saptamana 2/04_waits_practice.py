"""
IMPLICIT WAIT & EXPLICIT WAIT

LINK: https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
LINK = "https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver"
driver.get(LINK)
time.sleep(3)

driver.maximize_window()
time.sleep(3)

# ------- IMPLICIT WAIT --------

"""
1. Pe pagina https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver,
cand se face click pe butonul 'Change text to Selenium Webdriver',
dupa 10 secunde, textul din dreptul sau se va schimba
din 'site' in 'Selenium Webdriver'.

a.
- Apasa pe butonul 'Change Text to Selenium Webdriver'. 
- Identifica elementul cu textul 'Selenium Webdriver' dupa text si id (folosind XPATH).
Observa ce se intampla.
"""

# identificam butonul 'Change Text to Selenium Webdriver
change_text_btn = driver.find_element(By.ID, "populate-text")
change_text_btn.click()

# identificam elementul cu textul 'Selenium Webdriver' dupa text si id (XPATH)
changing_text_element = driver.find_element(By.XPATH, '//*[@id="h2" and contains(text(), "Selenium Webdriver")]')

# CONCLUZIE:
# Pentru ca incercam sa identificam elementul cu textul 'Selenium Webdriver' fara a seta un timp de asteptare,
# acesta nu va fi gasit (el se afiseaza doar dupa 10 secunde)


"""
b.
- Seteaza un implicit wait de 5 secunde.
- Apasa pe butonul 'Change Text to Selenium Webdriver'.
- Identifica elementul cu textul 'Selenium Webdriver' dupa text si id (folosind XPATH).
Observa ce se intampla
"""
# driver.implicitly_wait(5)

# identificam butonul 'Change Text to Selenium Webdriver
change_text_btn = driver.find_element(By.ID, "populate-text")
change_text_btn.click()

# identificam elementul cu textul 'Selenium Webdriver' dupa text si id (XPATH)
changing_text_element = driver.find_element(By.XPATH, '//*[@id="h2" and contains(text(), "Selenium Webdriver")]')

# CONCLUZIE:
# Pentru ca incercam sa identificam elementul cu textul 'Selenium Webdriver' cu un timp
# de asteptare mai mic decat cel necesar pentru ca elementul sa fie disponibil pe pagina,
# elementul respectiv NU va fi gasit!


"""
c. 
- Seteaza un implicit wait de 11 secunde.
- Apasa pe butonul 'Change Text to Selenium Webdriver'.
- Identifica elementul cu textul 'Selenium Webdriver' dupa text si id (folosind XPATH).
Observa ce se intampla
"""
driver.implicitly_wait(11)

# identificam butonul 'Change Text to Selenium Webdriver
change_text_btn = driver.find_element(By.ID, "populate-text")
change_text_btn.click()

# daca avem un element care nu este disponibil pe pagina
# se cauta timp de cate secunde sunt setate ca implicit wait
# si daca nu se gaseste dupa nici ce trec secundele respective
# vom avea eroare
change_text_btn = driver.find_element(By.ID, "p-text")
change_text_btn.click()

# identificam elementul cu textul 'Selenium Webdriver' dupa text si id (XPATH)
changing_text_element = driver.find_element(By.XPATH, '//*[@id="h2" and contains(text(), "Selenium Webdriver")]')

# CONCLUZIE:
# S-a asteptat timpul necesar pentru ca elementul sa fie disponibil pe site,
# astfel ca elementul a putut fi gasit.

# ------- EXPLICIT WAIT --------

"""
2. Identifica acelasi element (cel cu textul "Selenium Webdriver"),
setand in explicit wait de 11 secunde.
"""

# declaram un obiect din clasa WebDriverWait de 11 secunde
# aici definim doar wait-ul/timpul de asteptare
# asteptarea inca nu incepe
wait = WebDriverWait(driver, 11)

# identificam butonul 'Change Text to Selenium Webdriver'
change_text_btn = driver.find_element(By.ID, "populate-text")
change_text_btn.click()

wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="h2" and contains(text(), "Selenium Webdriver")]')))

# aici apare eroare instant
# pt ca elementul cu id-ul p-text nu este disponibil
# pe pagina si nici nu avem un timp setat specific pentru
# identificarea acestuia
change_text_btn = driver.find_element(By.ID, "p-text")
change_text_btn.click()

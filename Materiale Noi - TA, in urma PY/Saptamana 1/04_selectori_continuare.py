"""
Continuare SELECTORI:

- CLASS_NAME
- NAME
- TAG_NAME
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# varianta RECOMANDATA de creare driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# accesam un link
LINK = "https://demo.nopcommerce.com/register?returnUrl=%2F"
driver.get(LINK)
time.sleep(1)

# maximizam fereastra
driver.maximize_window()
time.sleep(1)

"""
CLASS NAME SELECTOR:

- Il folosim pentru a identifica elementele HTML care au atributul class.
- Atributul class este folosit pentru a grupa anumite elemente in functie
de caracteristici comune.

! DEZAVANTAJ: De cele mai multe ori, o clasa nu este unica pentru un element,
motiv pentru care va trebui sa il folosim in tot felul de combinatii (cu alte elemente)
pentru a identifica elementul respectiv in mod unic.

ATENTIE: Daca in valoarea atributului class avem spatii, inseamna ca avem mai multe
clase atribuite acelui element HTML

Exemplu:
<div class='form-control'>...</div> (1 clasa)
<div class='mt-2 bg-3 lg-5'>...</div> (3 clase)
"""

# identificam div-ul care contine textul "Your Personal Details"
# [class="title"]

element1 = driver.find_element(By.CLASS_NAME, "title")

"""
ATENTIE:

- sunt mai multe elemente cu clasa title si astfel nu vom
identifica elementul nostru intr-un mod UNIC

- norocul nostru este ca acest element este chiar primul element cu
aceasta clasa, motiv pentru care merge identificarea
(metoda find_element ne identifica primul element cu clasa respectiva)

- nu ne bazam pe noroc -> structura paginii web se poate schima, si
atunci identificarea noastra nu va mai merge corespunzator
"""

# identificarea mai multor elemente dupa un selector
div_elements = driver.find_elements(By.CLASS_NAME, "title")
print(div_elements) # o lista cu obiecte de tip WebElement

assert len(div_elements) == 9

# identificarea unui element care are atributul class
# si ii sunt aribuite mai mult de 1 clasa
# <ul class="top-menu notmobile">..</ul>
# [class="top-menu notmobile"]

# v1
driver.find_element(By.CLASS_NAME, "top-menu")

# v2
driver.find_element(By.CLASS_NAME, "notmobile")


"""
NAME SELECTOR

- Il folosim atunci cand dorim sa identificam elemente HTML
care au atributul name
"""

# identificam inputul pentru First Name, dupa atributul name
element2 = driver.find_element(By.NAME, "FirstName")

"""
TAG_NAME selector

- Il folosim ca sa identificam un element dupa tipul de tag
- Rar folosit, nu asigura unicitatea identificarii!
"""

driver.find_element(By.TAG_NAME, "form")

div_list = driver.find_elements(By.TAG_NAME, "div")
print(len(div_list))
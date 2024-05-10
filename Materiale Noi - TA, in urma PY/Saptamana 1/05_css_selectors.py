"""
Continuare SELECTORI:

- CSS SELECTORS = un sir de caractere utilizat pentru a identifica elemente in codul HTML cu scopul de a putea
interactiona cu acestea si de a le verifica functionalitatea.

"""

"LINK: https://the-internet.herokuapp.com/login"

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
time.sleep(1)

# accesam un link
LINK = 'https://the-internet.herokuapp.com/login'
driver.get(LINK)
time.sleep(1)

# maximizam fereastra
driver.maximize_window()
time.sleep(1)

"""
1. CSS SELECTOR - identificare dupa ID  ( se pune # inainte de valoarea id-ului_

Identifica inputul username dupa id, folosind CSS SELECTOR
"""
username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("tomsmith")
time.sleep(1)

"""
2. CSS SELECTOR - identificare dupa clasa  (se pune . inainte de valoarea clasei)

a. Identifica elementul h4 dupa clasa, folosim CSS SELECTOR

b. Identifica primul element cu clasele large-6, small-12, columns, folosind CSS SELECTOR.
Folosind assert, verifica daca tag-ul acestuia este div.
"""

# a
h4_element = driver.find_element(By.CSS_SELECTOR, ".subheader")

# b
# .class1.class2.class3
element = driver.find_element(By.CSS_SELECTOR, ".large-6.small-12.columns")
assert element.tag_name == 'div'

"""
3. CSS SELECTOR - identificare dupa nume tag + id/clasa

a. Identifica elementul form, dupa tag + id, folosind CSS SELECTOR.
Verifica ca atributul method al acestuia are valoarea 'post'

b. Identifica butonul de login dupa tag + clasa, folosind CSS SELECTOR.
Verifica ca textul acestuia este 'Login'
"""

# a
form_element = driver.find_element(By.CSS_SELECTOR, "form#login")
expected = 'post'
actual = form_element.get_attribute("method")
assert expected == actual

# b
login_btn = driver.find_element(By.CSS_SELECTOR, "button.radius")
actual = login_btn.text
expected = 'Login'

assert actual == expected
"""
4. CSS SELECTOR - identificare dupa tip atribut=valoare

Identifica label-ul pentru parola dupa atribut=valoare, folosind CSS SELECTOR.
Verifica ca textul acestuia este cel așteptat.
"""

# *[for='password'] -> cautam orice element (indiferent de tag) care are atributul
# for cu valoarea 'password'

# label[for='password'] - > cautam elementele/elementul cu tag-ul label care are atributul
# for cu valoarea 'password'

label_element = driver.find_element(By.CSS_SELECTOR, "label[for='password']")
expected = "Password"
actual = label_element.text

assert expected == actual

"""
5. CSS SELECTOR - identificare element mergând din copil in copil (>)

Identifica link-ul din footer (Elemental Selenium), pornind de la div-ul
cu id-ul "page-footer" folosind CSS SELECTOR, si mergând din copil in copil.
Verifica ca valoarea atributului href este cea așteptata.
"""
footer_link = driver.find_element(By.CSS_SELECTOR, "div#page-footer>div>div>a")
expected = "http://elementalselenium.com/"
actual = footer_link.get_attribute("href")

assert expected == actual


"""
6. CSS SELECTOR - identificare orice copil

Identifica link-ul din footer (Elemental Selenium), pornind de la div-ul
cu id-ul "page-footer" folosind CSS SELECTOR, sărind direct la acesta.

Verifica ca tag-ul acestuia este un tag a
"""

footer_link2 = driver.find_element(By.CSS_SELECTOR, "div#page-footer a")

"""
7. CSS SELECTOR - identificarea primului copil (first-of-type)

Identifica primul div ce apartine de tag-ul form si verifica ca are clasa row.
"""

# identificam primul copil direct al elementului cu tag-ul form, care
# are tag-ul div
# form > div:first-of-type

"""
8. CSS SELECTOR - identificarea ultimului copil (last-of-type)

Identifica copilul ultimului div ce apartine de tag-ul form
si verifica ca acesta are 3 clase setate.
"""

div_element = driver.find_element(By.CSS_SELECTOR, "form > div:last-of-type > div")
classes_as_str = div_element.get_attribute("class")
classes_list = classes_as_str.split()
assert len(classes_list) == 3


"""
9. CSS SELECTOR - identificare copil care nu este nici primul, nici ultimul (nth-of-type)

Acceseaza elementul input ce aparține de al doilea copil al elementului form
si verifica ca are id-ul setat corespunzător
"""
# form > *:nth-of-type(2) > div > input
# form > *:nth-of-type(2) input

"""
10. CSS SELECTOR - identificare frate ulterior (+)

Cauta elementul input care are ca si frate un label cu atributul for=username.

Verifica ca acesta are atributul type=text
"""
# label[for='username'] + input

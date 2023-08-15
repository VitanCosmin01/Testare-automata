"""
XPATH

XPATH = Selector care ne permite navigarea intr-un cod HTML.

Putem folosi XPATH, atunci cand niciuna din celalalte variante de
identificare nu ne-a putut ajuta sa gasim un element in interfata
in mod unic.

Tipuri XPATH:
1. XPATH absolut:
- identifica elementul pornind de la inceputul documentului pana in punctul in care
elementul este identificat
- click dreapta pe element, click pe copy, select full xpath
- exemplu: /html/body/div[1]/div/div/div[2]/div[4]/div/form/div[3]/button
- incepe cu un singur slash '/'. ca sa marcheze citirea de la inceputul documentului

2. XPATH relativ:
- identifica elementul pornind de la primul element unic gasit si navigand inainte sau inapoi pana ajungem
unde avem nevoie
- click dreapta pe element, click pe copy, select xpath
- exemplu: //buton[@type='submit' and @name='login-button']
- incepe cu doua slash-uri '//', ca sa marcheze citirea din interiorul documentului de la o anumita pozitie
"""
# https://the-internet.herokuapp.com/login

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
driver.
# cautare dupa tag
# //h4
# //form
# //input
# //form/div/div/input
# //form//input
element = driver.find_element(By.XPATH, "//h4")


# cautare dupa atribut = valoare pentru un tag specific
#//input[@name='username']
# //input[@type='text']
# //input[@type='text' and @name='username']

# cautare dupa atribut = valoare indiferent de tag
# //*[@type='text' and @name='username']

"""
XPATH - Axis Navigation

XPATH-ul ne ofera avantajul major ca poate sa efectueze urmatoarele tipuri de cautari:

- din parinte in copil
- din copil in parinte
- din element in frate ulterior
- din element in frate anterior

- PARINTE = orice element care are sub el mai multe elemente
- COPIL = orice element care se afla in componenta unui alt element
- FRATE ULTERIOR = orice element care se afla dupa un alt element sub acelasi parinte
- FRATE ANTERIOR = orice element care se afla inaintea unui alt element sub acelasi parinte
"""

# cautare din parinte in copil
# //form/div/div/input
# //form//input

# cautare din copil in parinte
# //input[@id='username']//parent::div
# //label[@for='username']//parent::div

# cautare element dupa text
# //*[contains(text(), 'Login Page')]
# //h2[contains(text(), 'Login')]
# //h2[text() = 'Login Page']

# cautare element dupa frati

# cautare dupa frate anterior - preceding-sibling

# Cautam fratele anterior cu tag-ul label, al elementului
# cu tag-ul input si atributul id ca fiind username
#//input[@id='username']//preceding-sibling::label

# cautare dupa frate ulterior - following-sibling
# //label[@for='username']//following-sibling::input
# //label[@for='username']//following-sibling::input[@type='text']

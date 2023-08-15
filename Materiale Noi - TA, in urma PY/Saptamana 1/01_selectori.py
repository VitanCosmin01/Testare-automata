"""
Intro HTML


Pagina HTML = orice pagina web este scrisa in limbajul HTML
Practic, pentru a defini structura/scheletul unei pagini web, avem nevoie de cod HTML.

Forma generala/ structura de baza a unei pagini/unui fisier HTML:

<html> - Primul tag din documentul HTML, este cel care va include intreg scheletul paginii web
       - Marcheaza inceputul paginii web

    <head>
        .... -> aici vom avea metadate (date despre date) care nu sunt afisate in browser
                (ex: titlul paginii, link-uri catre resurse externe - fisiere css, cdn-ul de bootstrap)
    </head>

    <body>

        .... -> aici avem continutul paginii (ceea ce apare in browser) (butoane, link-uri, imagini, paragrafe etc)

    </body>

</html>


Nodul <body> - contine toate elementele propriu-zise din pagina care sunt afisate in browser

- Fiecare element din pagina are un tip (un tag)
- Aceste tipuri sunt indicate prin <tag> HTML
- Orice element care se deschide cu un <tag> trebuie sa se si inchida cu un alt </tag> corespunzator
- Atentie: Exista elemente HTML self-closing! (adica care nu necesita un tag de inchidere)
- Fiecare element poate sa aiba unul sau mai multe atribute/proprietati.
- Aceste proprietati sunt definite la nivelul tag-ului de deschidere, si apar sub forma cheie="valoare"
- Exemple de atribute: id, name, class, placeholder, href
- Elementele HTML pot avea de asemenea si continut/text

Cele mai intalnite tag-uri HTML:

- <div> - division = marcheaza inceputul unei diviziuni
- <input> - input = o zona in care se pot introduce date de intrare/text
- <label> - eticheta = reprezinta o eticheta test care descrie un element sau un grup de elemente
- <a> - anchor/ancora = reprezinta un LINK, ceva pe care dam click
- <button> - buton = putem sa dam click si sa se intample o actiune
- <form> - formular = un formular alcatuit din mai multe elemente
- <h1> - heading 1 = un titlu care apare pe pagina (h1...h6)
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# import time
from time import sleep

"""
Libraria Selenium
"""

# instalare librarii necesare
# pip install selenium
# pip install webdriver-manager

# varianta simpla de instantiere browser
# driver = webdriver.Chrome()

# varianta mai complicata dar mai avantajoasa
# deoarece nu mai depindem de browser-ul local
# (daca este instalat sau nu pe calculator)
# varianta RECOMANDATA!
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
sleep(3)

# accesam un link
driver.get("https://formy-project.herokuapp.com/form")
sleep(3)

# maximizam fereastra
driver.maximize_window()
sleep(3)

# ID
element = driver.find_element(By.ID, "first-name")
print(element)
element.send_keys("Cosmina")
sleep(3)

last_name_element = driver.find_element(By.ID, "last-name")
last_name_element.send_keys("Bacter")

print(last_name_element.tag_name)
assert last_name_element.tag_name == 'input', "Tag-ul ar trebui sa fie input"
sleep(3)

# LINK TEXT
link_element = driver.find_element(By.LINK_TEXT, "Submit")
link_element.click()
sleep(2)

# navigam inapoi
driver.back()
time.sleep(1)

# PARTIAL LINK TEXT
link_element2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Sub")
link_element2.click()

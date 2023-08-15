"""
TEORIE 1. Ce este selenium?

RASPUNS:
Selenium este o librarie care ne ajuta/ ne ofera functionalitatile necesare
astfel incat sa putem identifica si iteractiona cu elemente HTML dintr-o
aplicatie web.
"""

"""
TEORIE 2. Ce este un driver?

RASPUNS: Un driver este un obiect din clasa browser-ului pe care dorim sa il folosim.
Exemplu: Chrome, Firefox, Edge etc.

Instantiere browser:

- Varianta 1:

from selenium import webdriver

driver = webdriver.Chrome()

- Varianta 2:    varianta recomandata

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
"""

"""
TEORIE 3. Ce este un selector?

RASPUNS: Un selector este un sir de caractere care are rolul de a identifica unul sau mai multe elemente
intr-o pagina web, cu scopul de a interactiona cu ele in procesul de automatizare.

Tipuri selectori:
- ID
- LINK_TEXT
- PARTIAL_LINK_TEXT
- NAME
- TAG_NAME
- CLASS_NAME
- CSS_SELECTOR
- XPATH
"""

"""
TEORIE 4. Ce metoda folosim pentru a identifica un element HTML
dintr-o pagina web si ce argumente ia aceasta metoda?

RASPUNS: find_element() - ia ca si parametri tipul de selector si
selectorul
"""

"""
TEORIE 5. Ce se intampla daca nu se gaseste niciun element HTML
dupa selectorul folosit?

RASPUNS: Se arunca o eroare: NoSuchElementException
"""


"""
TEORIE 6. Explica selectorul de tip ID

RASPUNS: Selectorul de tip ID il folosim atunci cand dorim sa identificam
un element HTML care are atributul id (acesta se gaseste in tag-ul de deschidere
al elementului respectiv).

Avantajul folosirii selectorului de tip ID, este ca in general, acesta ne va ajuta
sa identificam in mod unic un element deoarece in general id-urile sunt atribute cu valori unice
si specifice elementelor HTML.
"""

"""
TEORIE 7. Explica selectorul de tip LINK TEXT

RASPUNS: Selectorul de tip LINK_TEXT este cel care ne ajuta sa identificam un link dintr-o pagina web
(element HTML cu tag-ul a), furnizand textul COMPLET care apare peste acest link (cel pe care se da click).

Exemplu element a:

<a href="/products">Vezi produse</a>

identificarea in Python-> driver.find_element(By.LINK_TEXT, "Vezi produse")
"""

"""
TEORIE 8. Explica selectorul de tip PARTIAL LINK TEXT

RASPUNS: Selectorul de tip PARTIAL_LINK_TEXT este cel care ne ajuta sa identificam un link dintr-o pagina
 web (element HTML cu tag-ul a), furnizand textul PARTIAL care apare peste acest link (cel pe care se 
 da click).

Exemplu element a:

<a href="/products">Vezi produse</a>

identificarea in Python-> driver.find_element(By.PARTIAL_LINK_TEXT, "produse")
"""
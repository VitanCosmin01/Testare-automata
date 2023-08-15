"""
Situatii speciale -  WAIT-URI

- Exista unele situatii in care paginile se incarca mai greu,
ceea ce face ca elementele sa fie vizibile mai tarziu pe pagina,
ceea ce inseamna ca site-ul are o randare (rendering) ineficienta.

- Randarea (rendering) reprezinta procesul de transformare a codului
HTML, CSS si JavaScript intr-o pagina interactiva pe care vizitatorii
site-ului se asteapta sa o vada la interactiunea cu acea pagina.

- Ca sa putem rezolva aceasta problema, ne putem folosi de conceptele
de implicit wait si explicit wait.

1. IMPLICIT WAIT
- asteapta numarul definit de secunde inainte sa dea eroarea NoSuchElementException.
- util atunci cand avem un site care se incarca mai greu
- definit o singura data in cod, pe instanta de browser si acopera toate elementele cautate
pe acel driver: driver.implicitly_wait(6)

2. EXPLICIT WAIT
- Wait-urile explicite sunt putin diferite de implicit_wait(), deoarece ele se aplica o singura data (in momentul in care
 sunt apelate ca functie) existand mai multe conditii dupa care putem astepta sa fie indeplinite.

Exemple de conditii:
- prezenta elementului
- vizibilitatea elementului
- elementul sa contina un text
- atributul unui element sa existe
- atributul unui element sa contina o anumita valoare
- etc...

Structura unui explicit wait:

    wait = WebdriverWait(driver, x)
    wait.until(expected_condition)

unde:

    * WebdriverWait - este clasa care face driverul sa astepte
    * x - este cantitatea maxima de timp pana la indeplinirea conditiei (si inaintea returnarii unei erori)
    * expected_condition - conditia dupa care asteptam sa se indeplineasca

- ex:
username = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "username"))
username.send_keys("tomsmith")

EXEMPLU:

- Vrem sa cautam un element cu id-ul username pe un site.
Sistemul va cauta acel element, si daca il va gasi va trece instant la instructiunea urmatoare.

A. implicit wait
- Daca nu il gaseste, sistemul va continua sa il caute pe toata durata stabilita in implicit wait,
dupa care va da eroare.
- Daca nu am avea acel implicit wait, ar da eroare instant.

B. sleep
- Daca avem sleep inainte de element, atunci sistemul va astepta 5 secunde inainte sa caute elementul apoi il va cauta,
iar daca nu il va gasi, va da eroare instant.

- Daca avem sleep dupa element, o sa returneze eroare instant,
pentru ca sistemul nu mai ajunge sa execute instructiunea de sleep

C. explicit wait
- Daca avem explicit wait pe elementul cautat si acesta va fi gasit, va fi actionat asupra lui instant
- Daca avem explicit wait pe elementul cautat si acesta nu va fi gasit instant,
atunci se va astepta numarul de secunde definit, dupa care se va returna eroare in cazul in care
nu s-a gasit nici dupa numarul de secunde alocat.
- Daca avem explicit wait pe un alt element decat elementul cautat si acesta va fi gasit,
va fi actionat asupra lui instant
- Daca avem explicit wait pe  un alt element decat elementul cautat si acesta nu va fi gasit,
sistemul va returna eroare instant

"""
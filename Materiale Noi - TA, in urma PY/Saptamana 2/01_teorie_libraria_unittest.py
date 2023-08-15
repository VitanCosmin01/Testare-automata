"""
Libraria Unit Test

- unittest = librarie care suporta crearea de teste rulabile direct
in interiorul claselor
- a fost initial construita pentru realizarea testelor unitare (unit tests)
de catre echipa de dezvoltare (development).

- in contextul TESTARII AUTOMATE, desi ne putem folosi de aceeasi librarie
pentru a ne crea testele automate, nu facem testare unitara, care este in scopul
echipei de development.

- CUM NE FOLOSIM DE LIBRARIA UNITTEST IN COD?

1. importam libraria: import unittest
2. ne definim o clasa care sa cuprinda testele noastre.
    - aceasta clasa va trebui sa mosteneasca din clasa unittest.TestCase
    - denumirea clasei de test va incepe cu Test
    - exemplu: class TestAlerts(unittest.Testcase)

3. in interiorul clasei de teste, vom avea acces la doua metode speciale:
    - metoda setUp() -> definim toate activitatile care trebuie sa fie executate
inainte de ORICE TEST din clasa respectiva
    - metoda tearDown() -> definim toate activitatile care trebuie sa fie executate
dupa ORICE TEST din clasa respectiva

4. ne definim testele:
    - fiecare test este o metoda din clasa respectiva
    - denumirea acestor metode va incepe cu test_<descriere_scurta_test>

OBSERVATIE:
- In general, fiecare clasa trebuie sa contina metode de test inrudite
(adica care acopera aceeasi zona din aplicatie) si care in general
sunt conditionate de acelasi set de preconditii
(ex: toate testele de login trebuie sa porneasca de pe pagina de login,
toate testele de search product pleaca de la actiunea initiala de cautare produs etc.)

CUM RULAM TESTELE?

- Pentru rularea testelor avem mai multe variante:

1. Click pe triunghiul verde de langa numele clasei de test
- astfel, rulam toate testele din acea clasa
2. Click pe triunghiul verde de langa numele metodei de test
- astfel, se va executa/rula doar testul respectiv.
3. Rularea din terminal a unui fisier de teste specific:
- python -m unittest filename.py
4. Rularea din terminal a tuturor fisierelor de test:
python -m unittest

CUM DAM SKIP LA UN TEST LA RULARE?

- Atunci cand vrem sa sarim unele teste la rulare ne putem folosi
de decoratorul @unittest.skip plasat inaintea fiecarei metode de test
care se doreste a fi sarita
"""
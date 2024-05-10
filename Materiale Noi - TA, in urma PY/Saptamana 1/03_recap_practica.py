"""
1. Navigheaza catre urmatorul LINK: https://demo.nopcommerce.com/
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
LINK = "https://demo.nopcommerce.com/"
driver.get(LINK)
time.sleep(1)

# maximizam fereastra
driver.maximize_window()
time.sleep(1)

"""
2. Verifica ca titlul paginii este cel asteptat.
"""
expected_title = "nopCommerce demo store"

# accesarea titlului paginii curente
actual_title = driver.title
print(actual_title)

assert expected_title == actual_title

"""
3. Da click pe Register
"""

# identificare dupa LINK TEXT
register_element = driver.find_element(By.LINK_TEXT, "Register")
register_element.click()
time.sleep(2)

"""
4. Selecteaza un gen (sectiunea Gender).
Verifica ca elementul gasit are atributul type cu valoarea 'radio'
"""

# identificare dupa ID
gender_input_element = driver.find_element(By.ID, "gender-male")

# verificare atribute element HTML
assert gender_input_element.get_attribute("type") == "radio"

gender_input_element.click()
time.sleep(2)


"""
5. Identifica elementul in care putem scrie prenumele.
Verifica ca elementul gasit are tag-ul corespunzator.
Scrie un prenume.
"""

# identificare dupa ID
first_name_element = driver.find_element(By.ID, "FirstName")

# verificare tag element
assert first_name_element.tag_name == "input"

first_name_element.send_keys("Mihai")
time.sleep(2)
"""
6. Identifica elementul in care putem scrie numele de familie.
Verifica ca elementul gasit are tag-ul corespunzator.
Scrie un nume de familie.
"""
# identificare dupa ID
last_name_element = driver.find_element(By.ID, "LastName")

# verificare tag element
assert last_name_element.tag_name == "input"

last_name_element.send_keys("Ionescu")
time.sleep(2)

"""
7. Identifica elementul in care putem scrie email-ul.
Verifica ca valoarea atributului name este cea asteptata.
Completeaza cu o adresa de email.
"""
# din fereastra de Inspect -> CTRL + F -> [id="Email"]
email_element = driver.find_element(By.ID, "Email")

# verificare atribut element HTML
assert email_element.get_attribute("name") == "Email"

# TAG -> numele tag-ului (a, input, div, p, h1, button etc)
# ATRIBUT -> caracteristic tag-ului de deschidere (id, name, class, data-name, for, href, src etc)
import random

email_element.send_keys(f"something{random.randint(1, 9999999)}@yahoo.ro")
time.sleep(2)

"""
8. Identifica elementele in care trebuie sa introduci parolele
si introdu aceeași parola (3 caractere) in ambele locuri.
Verifica ca apare mesajul de eroare așteptat.
"""

# identificare dupa ID
pwd_el = driver.find_element(By.ID, "Password")
pwd_el.send_keys("123")

confirm_pwd_el = driver.find_element(By.ID, "ConfirmPassword")
confirm_pwd_el.send_keys("123")

pwd_error_el = driver.find_element(By.ID, "Password-error")
actual_error_text = pwd_error_el.text
expected_error_text = "Password must meet the following rules:\nmust have at least 6 characters"

assert actual_error_text == expected_error_text

"""
9. Sterge parolele introdusa la punctul 6.
Introdu o parola din 10 caractere.
Introdu o parola de confirmare care sa nu coincida cu cea initiala.
Apasa pe butonul REGISTER.
Verifica ca apare mesajul de eroare asteptat.
"""
# stergem textul pe care l-am scris
pwd_el.clear()
confirm_pwd_el.clear()
time.sleep(3)

pwd_el.send_keys("0123456789")
confirm_pwd_el.send_keys("123456")

# identificare dupa ID
register_btn = driver.find_element(By.ID, "register-button")
register_btn.click()

not_matching_err_element = driver.find_element(By.ID, "ConfirmPassword-error")

# accesarea textului dintr-un element
actual_error = not_matching_err_element.text
expected_error = "The password and confirmation password do not match."

assert actual_error == expected_error
time.sleep(2)

"""
10. Sterge continutul introdus la parole de la punctul 7

Introdu doua parole identice si apasa pe butonul REGISTER.

Verifica ca in url-ul paginii curente se gaseste string-ul "registerresult"
"""
# ștergem continutul de pe elemente
pwd_el.clear()
confirm_pwd_el.clear()

pwd_el.send_keys("0123456789")
confirm_pwd_el.send_keys("0123456789")

print(f"BEFORE: {driver.current_url}")
register_btn.click()

current_url = driver.current_url
print(f"AFTER: {driver.current_url}")

assert "registerresult" in current_url
time.sleep(2)

"""
11. Inchide browser-ul.
"""
driver.quit()


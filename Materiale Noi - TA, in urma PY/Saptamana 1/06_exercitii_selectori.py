"""
1.
- Instantiaza un browser de Chrome.
- Acceseaza pagina https://the-internet.herokuapp.com/
- Maximizeaza fereastra
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver = webdriver.Chrome()
link = "https://the-internet.herokuapp.com/"
driver.get(link)
time.sleep(3)

driver.maximize_window()
time.sleep(3)
"""
2. Acceseaza link-ul Form Authentication, folosind un selector potrivit.
Incearca mai multe variante posibile.
"""
# accesarea link-ului
# driver.get("https://the-internet.herokuapp.com/login")
# time.sleep(3)

# varianta IDENTIFICARE By.LINK_TEXT

# form_authentication = driver.find_element(By.LINK_TEXT, value="Form Authentication")
# form_authentication.click()
# time.sleep(3)

# VARIANTA By.PARTIAL_LINK_TEXT

form_authentication = driver.find_element(By.PARTIAL_LINK_TEXT, "Form")
form_authentication.click()
time.sleep(5)

# VARIANTA BY TAG_name

# form_authentication = driver.find_element(By.TAG_NAME, value="login")    # NU STIU


"""
3. Identifica elementul ce contine textul "Login Page"
si verifica, folosind un assert, ca acest element are textul asteptat
"""
# Varianta SZolt
login_text = driver.find_element(By.TAG_NAME, "h2")
# login_button = driver.find_element(By.CLASS_NAME, "radius") # nu e cerut de exercitiu
assert login_text.text == "Login Page"
time.sleep(2)

# identificare dupa Xpath
# login_element = driver.find_elements(By.XPATH,"L/html/body/div[2]/div/div/h2")

# identificare dupa Tag_Name
# login_element`= driver.find_element(By.TAG_NAME, "h2")
# time.sleep(3)
"""
4. Identifica input-urile username si password,
introdu valori valide, si da click pe butonul login
"""
username_element = driver.find_element(By.ID, "username")
username_element.send_keys("tomsmith")
password_element = driver.find_element(By.ID, "password")
password_element.send_keys("SuperSecretPassword!")
login_element = driver.find_element(By.CLASS_NAME, "fa-sign-in")
login_element.click()
time.sleep(5)
"""
5. Verifica, folosind un assert ca ai ajuns pe pagina
https://the-internet.herokuapp.com/secure
"""

link1 = "https://the-internet.herokuapp.com/secure"
assert driver.current_url == link1

"""
6. Da click pe butonul logout
"""
logout = driver.find_element(By.LINK_TEXT, "Logout")  # corect
logout2 = driver.find_element(By.CLASS_NAME, "button.secondary.radius")  # corect
logout2.click()
"""
7. Introdu un username corect si o parola incorecta.
Identifica mesajul care apare si verifica in cod ca acela este mesajul asteptat.
"""
username_element = driver.find_element(By.ID, "username")
username_element.send_keys("tomsmith")
password_element = driver.find_element(By.ID, "password")
password_element.send_keys("123")
login_element = driver.find_element(By.CLASS_NAME, "fa-sign-in")
login_element.click()
time.sleep(5)

error_element = driver.find_element(By.ID, "flash")
print(error_element.text)
# v1
# expected_error = "Your password is invalid!\n"
# assert expected_error == error_element.text

# v2
assert "Your password is invalid!" in error_element.text

"""
8. Introdu un username corect.
Gaseste elementul cu tag-ul h4.
Ia textul de pe el si fa split dupa spatiu. Considera fiecare cuvant ca o potentiala parola.
Foloseste o structura iterativa prin care sa introduci rand pe rand parolele si sa apesi login
La final, testul trebuie sa printeze fie "Nu am reusit sa gasesc parola", fie "Parola secreta este
[parola]"
"""

h4_element = driver.find_element(By.TAG_NAME, "h4")
possible_passwords = h4_element.text.split()
print(possible_passwords)
# possible_passwords[16] = 'parolaincorecta'
# print(possible_passwords)
for pwd in possible_passwords:
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")
    password = driver.find_element(By.ID, "password")
    password.send_keys(pwd)

    btn = driver.find_element(By.CLASS_NAME, "radius")
    btn.click()
    if driver.current_url == "https://the-internet.herokuapp.com/secure":
        print(f"Parola secreta este {pwd}")
        break
else:
    print("Nu am reusit sa gasesc parola")


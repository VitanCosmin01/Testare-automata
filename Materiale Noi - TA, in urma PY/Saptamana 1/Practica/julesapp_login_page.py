from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
time.sleep(3)

# accesam un link
driver.get("https://jules.app/sign-in")
# maximizam fereastra
driver.maximize_window()
time.sleep(3)

# identificam si introducem datele de conectare
email_element = driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']")
email_element.send_keys("vitan.cosmin83@gmail.com")
time.sleep(3)

password_element = driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']")
password_element.send_keys("Vc123123")
time.sleep(3)

login_button = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/form/div/div[3]/button")
login_button.click()
time.sleep(3)

# identificam mesajul de eroare pentru user neinregistrat daca rextul corespunde

text_error_elem = driver.find_element(By.XPATH, "//*[@id='client-snackbar']/div/span")
actual_error_text = text_error_elem.text
expected_error_text = "Invalid email/password combination"
assert actual_error_text == expected_error_text

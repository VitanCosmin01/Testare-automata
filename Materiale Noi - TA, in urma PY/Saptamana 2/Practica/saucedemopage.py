from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome()   # se foloseste doar pentru varianta simpla de instantiere a driver-ului
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(3)

username_element = driver.find_element(By.ID, "user-name")
username_element.send_keys("standard_user")
time.sleep(2)

password_element = driver.find_element(By.ID, "password")
password_element.send_keys("secret_sauce")
time.sleep(2)

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(2)

expected_url = "https://www.saucedemo.com/inventory.html"
actual_url = driver.title
assert expected_url, actual_url

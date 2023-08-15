"""
ALERTE

LINK: https://the-internet.herokuapp.com/javascript_alerts
"""
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
TESTE:

1. SIMPLE JS ALERT
- dam accept

2. CONFIRM JS ALERT
- dam accept
- dam cancel

3. PROMPT JS ALERT
- acceptam alerta fara a introduce text
- acceptam alerta cand introducem text

- dam cancel la alerta fara a introduce text
- dam cancel la alerta cand introducem text
"""


class TestAlerts(unittest.TestCase):
    LINK = "https://the-internet.herokuapp.com/javascript_alerts"
    BUTTON_JS_ALERT_SIMPLE = (By.XPATH, "//button[@onclick='jsAlert()']")
    BUTTON_JS_ALERT_CONFIRM = (By.XPATH, "//button[@onclick='jsConfirm()']")
    BUTTON_JS_ALERT_PROMPT = (By.XPATH, "//button[@onclick='jsPrompt()']")
    P_TEXT = (By.ID, "result")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_accept_simple_alert(self):
        """
        1. SIMPLE JS ALERT
            - dam accept
        """

        # dam click pe butonul 'Click for JS Alert'
        simple_alert_btn = self.driver.find_element(*self.BUTTON_JS_ALERT_SIMPLE)
        simple_alert_btn.click()
        time.sleep(2)

        # declaram o variabila pentru alerta, ca sa putem interactiona cu ea
        alert = self.driver.switch_to.alert

        # apasam butonul care accepta alerta (Ok)
        alert.accept()
        time.sleep(2)

        p_text_element = self.driver.find_element(*self.P_TEXT)
        expected_text = "You successfully clicked an alert"
        actual_text = p_text_element.text

        self.assertEqual(expected_text, actual_text)

    def test_accept_confirm_alert(self):
        """
        2. CONFIRM JS ALERT
            - dam accept
        """
        # dam click pe butonul 'Click for JS Confirm'
        confirm_alert_btn = self.driver.find_element(*self.BUTTON_JS_ALERT_CONFIRM)
        confirm_alert_btn.click()
        time.sleep(2)

        # declaram o variabila pentru alerta, ca sa putem interactiona cu ea
        alert = self.driver.switch_to.alert

        # apasam butonul care accepta alerta (Ok)
        alert.accept()
        time.sleep(2)

        p_text_element = self.driver.find_element(*self.P_TEXT)
        expected_text = "You clicked: Ok"
        actual_text = p_text_element.text

        self.assertEqual(expected_text, actual_text)

    def test_cancel_confirm_alert(self):
        """
        2. CONFIRM JS ALERT
            - dam cancel
        """
        # dam click pe butonul 'Click for JS Confirm'
        confirm_alert_btn = self.driver.find_element(*self.BUTTON_JS_ALERT_CONFIRM)
        confirm_alert_btn.click()
        time.sleep(2)

        # declaram o variabila pentru alerta, ca sa putem interactiona cu ea
        alert = self.driver.switch_to.alert

        # apasam butonul care da cancel la alerta (Cancel)
        alert.dismiss()
        time.sleep(2)

        p_text_element = self.driver.find_element(*self.P_TEXT)
        expected_text = "You clicked: Cancel"
        actual_text = p_text_element.text

        self.assertEqual(expected_text, actual_text)

    def test_accept_prompt_alert_without_text(self):
        """
        3. PROMPT JS ALERT
            - acceptam alerta fara a introduce text
        """
        # dam click pe butonul 'Click for JS Prompt'
        prompt_alert_btn = self.driver.find_element(*self.BUTTON_JS_ALERT_PROMPT)
        prompt_alert_btn.click()
        time.sleep(2)

        # declaram o variabila pentru alerta, ca sa putem interactiona cu ea
        alert = self.driver.switch_to.alert

        # apasam butonul care da accept la alerta
        # fara sa introducem un text inainte (butonul Ok)
        alert.accept()
        time.sleep(2)

        p_text_element = self.driver.find_element(*self.P_TEXT)
        expected_text = "You entered:"
        actual_text = p_text_element.text

        self.assertEqual(expected_text, actual_text)

    def test_accept_prompt_alert_with_text(self):
        """
        3. PROMPT JS ALERT
            - acceptam alerta cand introducem text
        """
        # dam click pe butonul 'Click for JS Prompt'
        prompt_alert_btn = self.driver.find_element(*self.BUTTON_JS_ALERT_PROMPT)
        prompt_alert_btn.click()
        time.sleep(2)

        # declaram o variabila pentru alerta, ca sa putem interactiona cu ea
        alert = self.driver.switch_to.alert

        # scriem un text in inputul de la alerta
        alert.send_keys("abc")
        time.sleep(3)

        # apasam butonul care da accept la alerta (butonul Ok)
        alert.accept()
        time.sleep(2)

        p_text_element = self.driver.find_element(*self.P_TEXT)
        expected_text = "You entered: abc"
        actual_text = p_text_element.text

        self.assertEqual(expected_text, actual_text)

    def test_cancel_prompt_alert_without_text(self):
        """
        3. PROMPT JS ALERT
            - dam cancel la alerta fara a introduce text
        """
        # dam click pe butonul 'Click for JS Prompt'
        prompt_alert_btn = self.driver.find_element(*self.BUTTON_JS_ALERT_PROMPT)
        prompt_alert_btn.click()
        time.sleep(2)

        # declaram o variabila pentru alerta, ca sa putem interactiona cu ea
        alert = self.driver.switch_to.alert

        # apasam butonul care da cancel la alerta
        # fara sa introducem un text inainte (butonul Cancel)
        alert.dismiss()
        time.sleep(2)

        p_text_element = self.driver.find_element(*self.P_TEXT)
        expected_text = "You entered: null"
        actual_text = p_text_element.text

        self.assertEqual(expected_text, actual_text)

    def test_cancel_prompt_alert_with_text(self):
        """
        3. PROMPT JS ALERT
            - dam cancel la alerta cand introducem text
        """
        # dam click pe butonul 'Click for JS Prompt'
        prompt_alert_btn = self.driver.find_element(*self.BUTTON_JS_ALERT_PROMPT)
        prompt_alert_btn.click()
        time.sleep(2)

        # declaram o variabila pentru alerta, ca sa putem interactiona cu ea
        alert = self.driver.switch_to.alert

        # scriem un text in inputul de la alerta
        alert.send_keys("abc")
        time.sleep(3)

        # apasam butonul care da cancel la alerta (butonul Cancel)
        alert.dismiss()
        time.sleep(2)

        p_text_element = self.driver.find_element(*self.P_TEXT)
        expected_text = "You entered: null"
        actual_text = p_text_element.text

        self.assertEqual(expected_text, actual_text)

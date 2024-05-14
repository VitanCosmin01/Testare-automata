from selenium import webdriver


class Browser:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()

    def close(self):
        self.browser.close()

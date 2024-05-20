from base_page import BasePage


class DetailsPage(BasePage):

    def check_current_url(self):
        expected_url = "https://www.saucedemo.com/inventory-item.html?id=4"
        actual_url = self.browser.current_url
        assert expected_url == actual_url
        
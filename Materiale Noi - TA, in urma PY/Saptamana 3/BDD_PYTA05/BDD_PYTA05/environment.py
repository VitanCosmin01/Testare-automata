from browser import Browser
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def before_all(context):
    """
    Vom defini toate instructiunile care trebuie
    executate inaintea rularii tuturor pasilor
    """
    context.browser = Browser()
    context.login_page = LoginPage()
    context.products_page = ProductsPage()


def after_all(context):
    """
    Vom defini toate instructiunile care trebuie
    executate dupa rularea tuturor pasilor
    """
    context.browser.close()

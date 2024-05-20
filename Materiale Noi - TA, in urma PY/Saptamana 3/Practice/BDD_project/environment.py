from browser import Browser
from pages.details_page import DetailsPage
from pages.products_page import ProductPage


def before_all(context):
    context.browser = Browser()
    context.products_page = ProductPage()
    context.details_page = DetailsPage()


def after_all(context):
    context.browser.close()

from behave import *


# Scenariu 1
@given("I am on the product's page")
def step_impl(context):
    context.products_page.navigate_to_product_page()


@when("I click on the product's name")
def step_impl(context):
    context.products_page.click_name()


@then("I go to product's detailpage")
def step_impl(context):
    context.details_page.check_current_url()


# Scenariul 2
@when("I click on the product's picture")
def step_impl(context):
    context.products_page.click_picture()


# Scenariu 3
@when("I click the button Add to cart")
def step_impl(context):
    context.products_page.add_to_cart()


@then("The product is added to the cart")
def step_impl(context):
    context.products_page.add_to_cart()
    context.products_page.check_kart()

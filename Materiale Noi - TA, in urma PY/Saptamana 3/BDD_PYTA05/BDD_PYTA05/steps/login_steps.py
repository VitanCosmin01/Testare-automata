from behave import *


@given("I am on the saucedemo login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when("I insert the correct username and correct password")
def step_impl(context):
    context.login_page.insert_correct_username()
    context.login_page.insert_correct_password()


@when("I click the login button")
def step_impl(context):
    context.login_page.click_login_button()


@then("I can login into the application and see the list of products")
def step_impl(context):
    # trebuie sa apelam metoda check_current_url
    # disponibila in clasa ProductsPage
    context.products_page.check_current_url()


@when("I insert the correct username and incorrect password")
def step_impl(context):
    context.login_page.insert_correct_username()
    context.login_page.insert_incorrect_password()


@then("I can't login into the application and receive error Epic sadface: Username and password do not match any user in this service")
def step_impl(context):
    context.login_page.check_error_message_invalid_pwd()

# Scenario 3
@when("I insert the incorrect username and correct password")
def step_impl(context):
    context.login_page.insert_incorrect_username()
    context.login_page.insert_correct_password()

# Scenario 4
@when("I insert the valid username and  no password")
def step_impl(context):
    context.login_page.insert_correct_username()

@then("I can't login into the application and receive error Epic sadface: Password is required")
def step_impl(context):
    context.login_page.check_error_message_password_required()

# Scenario 5
@when("I insert username none and a valid password")
def step_impl(context):
    context.login_page.insert_correct_password()

@then("I can't login into the application and receive error Epic sadface: Username is required")
def step_impl(context):
    context.login_page.check_error_message_username_required()

# Scenario 6
@when("I insert username none and password none")
def step_impl(context):
    context.login_page.check_error_message_username_required()

# Scenario 7
@when("I insert incorrect username and password is none")
def step_impl(context):
    context.login_page.check_error_message_password_required()

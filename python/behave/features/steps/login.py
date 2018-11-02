from behave import *
import time


@given("the user is on the home page")
def step_impl(context):
    context.browser.get('https://sprinkle-burn.glitch.me/')
    time.sleep(2)


@when('the user enters username as "{email}"')
def step_impl(context, email):
    if email == "empty":
        context.browser.find_element_by_name("email").send_keys(' ')
    else:
        context.browser.find_element_by_name("email").send_keys(email)


@step('the user enters password as "{password}"')
def step_impl(context, password):
    if password == "empty":
        context.browser.find_element_by_name("email").send_keys(' ')
    else:
        context.browser.find_element_by_name("password").send_keys(password)


@step("clicks Login")
def step_impl(context):
    time.sleep(4)
    context.browser.find_element_by_xpath("//div/button[text()='Login']").click()
    time.sleep(2)


@then('the user is presented with a welcome message as "{welcome_msg}"')
def step_impl(context, welcome_msg):
    welc_msg = context.browser.find_element_by_xpath("//article[@class='pa4 black-80 content']").text
    assert welc_msg == welcome_msg


@then('the user is presented with an error message as "{error_msg}"')
def step_impl(context, error_msg):
    err_msg = context.browser.find_element_by_xpath("//div[@id='login-error-box']").text
    assert err_msg == error_msg





from behave import *
from selenium import webdriver




@given('Open the browser')
def browser(context):
    context.driver.get("https://rahulshettyacademy.com/angularpractice/")

@when('Enter username "{user}" and email "{email}"')
def details(context,user,email):
    context.driver.find_element_by_name("name").send_keys(user)
    context.driver.find_element_by_name("email").send_keys(email)





@when('Click submit')
def submit(context):
    context.driver.find_element_by_css_selector("[type='submit']").click()



@then('Verify message')
def step_impl(context):
    message =context.driver.find_element_by_css_selector("[class='alert alert-success alert-dismissible']").text
    assert "Success" in message
    print(message)
    context.driver.close()



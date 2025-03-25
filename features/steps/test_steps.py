import os
from behave import given, when, then


@given("the user is logged in")
def step_impl(context):
    context.login_page.enter_login_username(context.test_username)
    context.login_page.enter_login_password(context.test_password)
    context.login_page.click_login_button()
    assert context.login_page.check_login_status()

@when('the user adds an item "{item_name}" to the cart')
def step_impl(context,item_name):
    if item_name not in context.test_data["items"]:
        raise ValueError(f"Item '{item_name}' not found in test data")
    context.home_page.click_add_to_cart_button(item_name)

@when("the user opens the cart page")
def step_impl(context):
    context.home_page.navigate_to_cart()

@then('the cart contains the item "{item_name}"')
def step_impl(context,item_name):
    assert context.cart_page.is_item_in_cart(item_name)

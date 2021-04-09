from behave import given, when, then



@given('Open Lost Password page')
def open_lost_password_page(context):
    context.app.lost_password_page.open_lost_password_page()


@then('Verify page has correct UI elements')
def verify_correct_ui_elements(context):
    context.app.lost_password_page.verify_correct_ui_elements()


@then('Verify user can see Best Selling, Latest, Top Rated blocks')
def verify_category_blocks(context):
    context.app.lost_password_page.verify_product_blocks()


@when('Enter "test" for non-existing user in the input field')
def enter_invalid_information(context):
    context.app.lost_password_page.enter_invalid_information()


@when('Click on Reset Password button')
def click_reset_button(context):
    context.app.lost_password_page.click_reset_password()


@then('Verify a correct error message is displayed')
def verify_error_message(context):
    context.app.lost_password_page.verify_error_message()


@when('Enter "admin" for existing user in the input field')
def input_valid_information(context):
    context.app.lost_password_page.enter_valid_information()


@then('Verify a correct confirmation message is displayed')
def verify_confirmation_message(context):
    context.app.lost_password_page.verify_confirmation_message()


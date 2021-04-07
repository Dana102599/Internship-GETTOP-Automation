
from behave import given, when, then




@given('Open shop page')
def open_page(context):
    context.app.sort_by_latest_page.open_order_by_page()


@when('Select sort by latest')
def select_sort_by_latest(context):
    context.app.sort_by_latest_page.select_from_dropdown()


@then('Verify query “orderby=date“ will appear in page URL')
def verify_orderbydate_in_url(context):
    context.app.sort_by_latest_page.verify_orderbydate_in_url()


@then('Verify user can go through all product pages after they sorted by Latest')
def go_thru_all_product_pages(context):
    context.app.sort_by_latest_page.verify_product_pages_in_sort_by_latest()


@then('Verify user can reset to Default Sorting')
def reset_to_default_sorting(context):
    context.app.sort_by_latest_page.verify_reset_to_default_sorting()


@given('Open given URL')
def open_given_url(context):
    context.app.sort_by_latest_page.open_given_url()


@then('Verify given URL opens the page with products sorted by Latest')
def verify_url_open_correct_page(context):
    context.app.sort_by_latest_page.verify_url_opens_correct_page()





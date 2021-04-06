
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SOCIAL_LOGO = (By.CSS_SELECTOR, ".icon-facebook")




@given('Open Gettop product page')
def open_product(context):
    context.app.product_page.open_product_page()


@then('Verify product has {} images')
def verify_products_has_image(context, expected_images):
    context.app.product_page.verify_product_images(expected_images)



@then('Verify product has name')
def verify_products_name(context):
    context.app.product_page.verify_product_name()


@then('Verify product has price')
def verify_products_price(context):
    context.app.product_page.verify_product_price()


@then('Verify product has description')
def verify_products_description(context):
    context.app.product_page.verify_product_description()


@when('Click on zoom icon')
def click_zoom_icon(context):
    context.app.product_page.click_zoom_icon()


@when('Scroll thru images')
def scroll_thru_images(context):
    context.app.product_page.scroll_thru_images()


@then('Close zoomed image by clicking X')
def close_zoomed_image(context):
    context.app.product_page.close_zoomed_image()


@when('Hover over product image')
def hover_over_heart_icon(context):
    context.app.product_page.hover_over_heart_icon()


@when('Click on heart icon')
def click_heart_icon(context):
    context.app.product_page.click_on_heart_icon()


@when('Click on wishlist icon')
def click_on_wishlist(context):
    context.app.product_page.click_on_wishlist()


@then('Verify item added to wishlist')
def verify_product_added(context):
    context.app.product_page.verify_product_added_message_popup()

@when('Click on "Home" link')
def click_home_link(context):
    context.app.product_page.click_on_home_link()


@then('Verify Home Page is displayed')
def verify_home_page_displayed(context):
    context.app.product_page.verify_home_page_displayed()


@when('Click on product category name')
def click_catergory_link(context):
    context.app.product_page.click_product_category()


@then('Verify correct category page is displayed')
def verify_category_page(context):
    context.app.product_page.verify_correct_category_page()


@then('Verify there are {expected_links} social logos present')
def verify_social_links(context, expected_links):
    context.app.product_page.verify_social_links_present(expected_links)


@when('Click on a social network link')
def click_on_social_network_logo(context):
    context.app.window_handling_page.store_current_window()
    context.app.product_page.click_on_social_network_logo()
    #context.original_window = context.driver.current_window_handle
    #context.driver.find_element(*SOCIAL_LOGO).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.window_handling_page.switch_to_new_window()
    # context.driver.wait.until(EC.new_window_is_opened)
    # context.driver.switch_to.window(context.driver.window_handles[1])


@then('Verify new window to login to social network is open')
def verify_page_is_open(context):
    context.app.product_page.verify_new_page_opens()


@then("User can close new window and switch back to original")
def close_and_switch_back(context):
    context.app.window_handling_page.close_and_switch_back()
    # context.driver.close()
    # context.driver.switch_to.window(context.original_window)


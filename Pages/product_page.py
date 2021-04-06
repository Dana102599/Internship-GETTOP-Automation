from Pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ProductPage(Page):

    PRODUCT_NAME = (By.CSS_SELECTOR,".entry-title" )
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-page-price")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, ".product-short-description" )
    ZOOM_ICON = (By.CSS_SELECTOR, ".icon-expand")
    ZOOMED_IMAGE = (By.CSS_SELECTOR, ".pswp__button--close")
    NEXT_ARROW = (By.CSS_SELECTOR, ".pswp__button--arrow--right")
    All_IMAGES = (By.XPATH, "//img[@width='600']")
    HEART_ICON = (By.CSS_SELECTOR, ".wishlist-icon")
    POPUP_MESSAGE = (By.CSS_SELECTOR, "#yith-wcwl-message")
    HOME_LINK = (By.XPATH, "//a[@href='https://gettop.us']")
    HOME_PAGE = (By.XPATH, "//div[@class='text dark']//p")
    CATEGORY_LINK = (By.XPATH,"//a[@href='https://gettop.us/product-category/macbook/']")
    CATEGORY_PAGE = (By.CSS_SELECTOR, ".woocommerce-breadcrumb")
    SOCIAL_LINKS = (By.CSS_SELECTOR, ".share-icons  i")
    NEW_PAGE = (By.CSS_SELECTOR, ".lfloat h2")
    SOCIAL_LOGO = (By.CSS_SELECTOR, ".icon-facebook")



    def open_product_page(self):
        self.open_url('https://gettop.us/product/macbook-air/')

    def verify_product_images(self, expected_images):
        actual_images = self.driver.find_elements(*self.All_IMAGES)
        assert len(actual_images) == int(expected_images), f' Expected {expected_images} links, but we see {len(actual_images)}'

    def verify_product_name(self):
        actual_text = self.driver.find_element(*self.PRODUCT_NAME).text
        expected_text = "MacBook Air"
        assert expected_text == actual_text, f"Expected {expected_text} does not match actual {actual_text}"

    def verify_product_price(self):
        actual_text = self.driver.find_element(*self.PRODUCT_PRICE).text
        expected_text = "$999.00"
        assert expected_text == actual_text, f"Expected {expected_text} does not match actual {actual_text}"

    def verify_product_description(self):
        actual_text = self.driver.find_element(*self.PRODUCT_DESCRIPTION).text
        expected_text = actual_text
        assert actual_text == expected_text, f"Expected {expected_text} does not match actual {actual_text}"

    def click_zoom_icon(self):
        self.click(*self.ZOOM_ICON)

    def scroll_thru_images(self):
        self.wait_for_element_appear(*self.All_IMAGES)
        all_images = self.driver.find_elements(*self.All_IMAGES)
        for i in range(len(all_images)):
            self.click(*self.NEXT_ARROW)

    def close_zoomed_image(self):
        self.click(*self.ZOOMED_IMAGE)

    def hover_over_heart_icon(self):
        heart_icon = self.find_element(*self.HEART_ICON)
        actions = ActionChains(self.driver)
        actions.move_to_element(heart_icon)
        actions.perform()

    def click_on_heart_icon(self):
        self.click(*self.HEART_ICON)

    def verify_product_added_message_popup(self):
        self.wait_for_element_appear(*self.POPUP_MESSAGE)

    def click_on_home_link(self):
        self.click(*self.HOME_LINK)

    def verify_home_page_displayed(self):
        actual_text = self.driver.find_element(*self.HOME_PAGE).text
        expected_text = "New"
        assert expected_text == actual_text, f"Expected {expected_text} does not match actual {actual_text}"

    def click_product_category(self):
        self.click(*self.CATEGORY_LINK)

    def verify_correct_category_page(self):
        actual_text = self.driver.find_element(*self.CATEGORY_PAGE).text
        expected_text = "HOME / MACBOOK"
        assert expected_text == actual_text, f"Expected {expected_text} does not match actual {actual_text}"

    def verify_social_links_present(self, expected_links):
        actual_links = self.driver.find_elements(*self.SOCIAL_LINKS)
        assert len(actual_links) == int(expected_links), f' Expected {expected_links} links, but we see {len(actual_links)}'

    def click_on_social_network_logo(self):
        self.click(*self.SOCIAL_LOGO)

    def verify_new_page_opens(self):
        actual_text = self.driver.find_element(*self.NEW_PAGE).text
        expected_text = "Facebook"
        assert expected_text == actual_text, f' Expected {expected_text}, but got {actual_text}'



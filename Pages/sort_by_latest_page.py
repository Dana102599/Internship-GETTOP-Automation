from Pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SortByLatest(Page):

    SELECT_DROPDOWN = (By.CSS_SELECTOR, ".orderby")
    PAGE_NUMBER = (By.CSS_SELECTOR, ".nav-pagination li")
    PAGE_HEADER = (By.CSS_SELECTOR, ".page-title")
    SELECTED_DEFAULT = (By.CSS_SELECTOR, "option[value='menu_order']")
    SORT_BY_LATEST = (By.CSS_SELECTOR, "option[value='date']")

    def open_order_by_page(self):
        self.open_url('https://gettop.us/shop/?orderby=menu_order')

    def open_given_url(self):
        self.open_url('https://gettop.us/shop/?orderby=date')

    def select_from_dropdown(self):
        select = Select(self.find_element(*self.SELECT_DROPDOWN))
        select.select_by_value("date")

    def verify_orderbydate_in_url(self):

        if "orderby=date" in self.driver.current_url:
         print("orderby=date in url")

    def verify_product_pages_in_sort_by_latest(self):
         page_number = self.driver.find_elements(*self.PAGE_NUMBER)
         self.driver.refresh()

         for x in range(len(page_number)):
            page = self.driver.find_elements(*self.PAGE_NUMBER)[x]
            page_text = page.text
            page.click()

            header_text = self.driver.find_element(*self.PAGE_HEADER).text
            assert page_text in header_text, f'Expected{page_text}  not in {header_text}'

    def verify_reset_to_default_sorting(self):
        select = Select(self.find_element(*self.SELECT_DROPDOWN))
        select.select_by_value("menu_order")

        actual_text = self.driver.find_element(*self.SELECTED_DEFAULT).text
        expected_text = "Default sorting"
        assert expected_text == actual_text, f"Expected {expected_text} does not match actual {actual_text}"

    def verify_url_opens_correct_page(self):
        actual_text = self.driver.find_element(*self.SORT_BY_LATEST).text
        expected_text = "Sort by latest"
        assert expected_text == actual_text, f"Expected {expected_text} does not match actual {actual_text}"






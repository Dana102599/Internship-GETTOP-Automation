from Pages.product_page import ProductPage
from Pages.window_handling_page import WindowHandling
from Pages.sort_by_latest_page import SortByLatest

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.product_page = ProductPage(self.driver)
        self.window_handling_page = WindowHandling(self.driver)
        self.sort_by_latest_page = SortByLatest(self.driver)
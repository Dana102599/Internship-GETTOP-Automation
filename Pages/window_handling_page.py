from Pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class WindowHandling(Page):

    def store_current_window(self):
        self.original_window = self.driver.current_window_handle

    def switch_to_new_window(self):
        self.driver.wait.until(EC.new_window_is_opened)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def close_and_switch_back(self):
        self.driver.close()
        self.driver.switch_to.window(self.original_window)
from Pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class AccountLostPassword(Page):

    FORM_UI_ELEMENTS = (By.CSS_SELECTOR, ".lost_reset_password p")
    CATEGORY_BLOCKS = (By.CSS_SELECTOR, ".widget-title")
    BLOCK_NAMES = ('BEST SELLING', 'LATEST', 'TOP RATED')
    INPUT_FIELD = (By.ID, "user_login")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".woocommerce-error li")
    RESET_PASSWORD_BTN = (By.CSS_SELECTOR, ".woocommerce-Button")
    CONFIRMATION_MESSAGE =(By.CSS_SELECTOR, ".woocommerce-message div")

    def open_lost_password_page(self):
        self.open_url('https://gettop.us/my-account/lost-password/')

    def verify_correct_ui_elements(self):
        elements = self.driver.find_elements(*self.FORM_UI_ELEMENTS)

        for i in range(len(elements)):
            print(elements[i].text)

    def verify_product_blocks(self):
        blocks = self.driver.find_elements(*self.CATEGORY_BLOCKS)
        for i in range(len(blocks)):
            assert blocks[i].text == self.BLOCK_NAMES[i]

    def enter_invalid_information(self):
        self.input_text('test',*self.INPUT_FIELD)

    def click_reset_password(self):
        self.click(*self.RESET_PASSWORD_BTN)

    def verify_error_message(self):
        self.verify_text('Invalid username or email.',*self.ERROR_MESSAGE)

    def enter_valid_information(self):
        self.input_text('admin',*self.INPUT_FIELD)

    def verify_confirmation_message(self):
        self.verify_text('Password reset email has been sent.', *self.CONFIRMATION_MESSAGE)






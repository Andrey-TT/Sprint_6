from locators.dzen_page_locators import DzenPageLocators
from pages.base_page import BasePage

class DzenPage(BasePage):
    def check_dzen_logo(self):
        return self.find_element(DzenPageLocators.LOGO_DZEN)
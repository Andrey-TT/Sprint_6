from locators.dzen_locators import DzenLocators
from pages.base_page import BasePage
import allure


class LogoDzen(BasePage):
    @allure.step('Проверка открытия страницы "Яндекс Дзен"')
    def check_dzen_logo(self):
        return self.find_element(DzenLocators.LOGO_DZEN)
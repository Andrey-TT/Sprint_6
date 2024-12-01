from pages.base_page import BasePage
from locators.main_locators import MainPageLocators, CookieBaLocator, OrderButtonLocators
import allure

class HomePage(BasePage):
    @allure.step('Получение текстов ответов')
    def check_answer_text(self, num):
        question = self.format_to_locator(MainPageLocators.QUESTION, num)
        answer = self.format_to_locator(MainPageLocators.ANSWER, num)
        self.scroll_to_element(MainPageLocators.QUESTION_8)
        self.click_element(CookieBaLocator.BUTTON_COOKIE)
        self.click_element(question)
        return self.get_text_from_element(answer)

class LogoYandex(BasePage):
    @allure.step('Клик на логотип "Яндекс" для открытия нового окна "Яндекс Дзен"')
    def click_logo_yandex(self):
        self.click_element(MainPageLocators.LOGO_YANDEX)

class OrderButten(BasePage):
    @allure.step('Переход к форме для заказа с помощью кнопки "Заказать" вверху страницы')
    def check_button_order_top(self):
        self.click_element(OrderButtonLocators.BUTTON_ORDER_TOP)
        return self.get_url()

    @allure.step('Переход к форме для заказа с помощью кнопки "Заказать" по центру страницы')
    def check_button_to_order_center(self):
        self.scroll_to_element(OrderButtonLocators.BUTTON_ORDER_CENTER)
        self.click_element(CookieBaLocator.BUTTON_COOKIE)
        self.click_element(OrderButtonLocators.BUTTON_ORDER_CENTER)
        return self.get_url()
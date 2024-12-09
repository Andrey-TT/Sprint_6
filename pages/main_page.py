from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def check_answer_text(self, num):
        question = self.format_to_locator(MainPageLocators.QUESTION, num)
        answer = self.format_to_locator(MainPageLocators.ANSWER, num)
        self.scroll_to_element(MainPageLocators.QUESTION_8)
        self.click_element(MainPageLocators.BUTTON_COOKIE)
        self.click_element(question)
        return self.get_text_from_element(answer)

    def click_logo_yandex(self):
        self.click_element(MainPageLocators.BUTTON_COOKIE)
        self.click_element(MainPageLocators.LOGO_YANDEX)

    def click_logo_scooter(self):
        self.click_element(MainPageLocators.LOGO_SCOOTER)

    def check_button_order_top(self):
        self.click_element(MainPageLocators.BUTTON_COOKIE)
        self.click_element(MainPageLocators.BUTTON_ORDER_TOP)
        return self.get_url()

    def check_button_to_order_center(self):
        self.scroll_to_element(MainPageLocators.BUTTON_ORDER_CENTER)
        self.click_element(MainPageLocators.BUTTON_COOKIE)
        self.click_element(MainPageLocators.BUTTON_ORDER_CENTER)

    def check_main_page_open(self):
        return self.find_element(MainPageLocators.TITLE_ABOUT_SCOOTER)
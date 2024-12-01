from pages.base_page import BasePage
from locators.order_locators import OrderPageLocators, CookieBaLocator, OrderForm1Locators, OrderForm2Locators, OrderPopUpLocators
import allure

class LogoScooter(BasePage):
    @allure.step('Клик на логотип "Самокат" для перехода на домашнюю страницу')
    def click_logo_scooter(self):
        self.click_element(OrderPageLocators.LOGO_SCOOTER)
        return self.get_url()

class OrderPage(BasePage):
    @allure.step('Заполнение формы для заказа')
    def add_user_data_to_form_order(self, name, last_name, address, metro, phone, date, rental_day,color, comment_for_courier):
        self.click_element(CookieBaLocator.BUTTON_COOKIE)
        self.add_text_to_element(OrderForm1Locators.NAME, name)
        self.add_text_to_element(OrderForm1Locators.LAST_NAME, last_name)
        self.add_text_to_element(OrderForm1Locators.ADDRESS, address)
        self.click_element(OrderForm1Locators.METRO)
        self.click_element(metro)
        self.add_text_to_element(OrderForm1Locators.PHONE, phone)
        self.click_element(OrderForm1Locators.NEXT)
        self.add_text_to_element(OrderForm2Locators.DATA_ORDER, date)
        self.click_element(OrderForm2Locators.TITLE_ABOUT_RENT)
        self.click_element(OrderForm2Locators.RENTAL_PERIOD)
        self.click_element(rental_day)
        self.click_element(color)
        self.add_text_to_element(OrderForm2Locators.COMMENT_FOR_COURIER, comment_for_courier)
        self.click_element(OrderForm2Locators.BUTTON_TO_ORDER_IN_FORM)
        return self.find_element(OrderPopUpLocators.BUTTON_YES_ORDER)

    @allure.step('Получение поп-апа об успешном оформлении заказа')
    def check_window_successful_order(self):
        self.click_element(OrderPopUpLocators.BUTTON_YES_ORDER)
        return self.get_text_from_element(OrderPopUpLocators.POP_UP_WINDOW_SUCCESSFUL_ORDER)

    @allure.step('Проверка открытия формы заказа')
    def check_order_page_open(self):
        return self.find_element(OrderForm2Locators.TITLE_ABOUT_RENT)



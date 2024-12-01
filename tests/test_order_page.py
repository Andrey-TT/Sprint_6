import allure
from conftest import driver
import pytest
from data import Url, OrderData
from pages.order_page import LogoScooter, OrderPage
from locators.order_locators import OrderForm1Locators, OrderForm2Locators

@allure.title('Тестирование перехода по клику на логотип Самокат')
class TestLogo:
    @allure.title('Кликаем на логотип "Самокат" и проверяем переход на страницу "Яндекс Самокат"')
    def test_check_logo_scooter_open_home_page(self, driver):
        driver.get(Url.order_page)
        logo = LogoScooter(driver)
        logo.click_logo_scooter()
        new_url = logo.click_logo_scooter()
        assert Url.main_page in new_url

@allure.title('Оформление заказа')
class TestOrderPage:
    @allure.title('Оформление заказа с разными тестовыми данными')
    @pytest.mark.parametrize("name, last_name, address, metro, phone, date, rental_day, color, comment_for_courier",
        [
            (OrderData.name_1, OrderData.last_name_1, OrderData.address_1, OrderForm1Locators.METRO_LUBANKA, OrderData.phone_1, OrderData.date_1, OrderForm2Locators.RENT_1_DAY, OrderForm2Locators.CHECKBOX_BLACK_COLOR, OrderData.comment_empty),
            (OrderData.name_2, OrderData.last_name_2, OrderData.address_2, OrderForm1Locators.METRO_SPORTIVNAY, OrderData.phone_2, OrderData.date_2, OrderForm2Locators.RENT_2_DAYS, OrderForm2Locators.CHECKBOX_GREY_COLOR, OrderData.comment_for_courier_1)
        ], ids=['Оформление заказа с данными первого пользователя', 'Оформление заказа с данными второго пользователя'])
    def test_order_with_different_user_data(self, driver, name, last_name, address, metro, phone, date, rental_day,color, comment_for_courier):
        driver.get(Url.order_page)
        order_page = OrderPage(driver)
        order_page.add_user_data_to_form_order(name, last_name, address, metro, phone, date, rental_day,color, comment_for_courier)
        success_screen_text = order_page.check_window_successful_order()
        assert 'Заказ оформлен' in success_screen_text

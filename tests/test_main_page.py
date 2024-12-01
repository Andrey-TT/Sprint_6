import allure
from conftest import driver
import pytest
from data import Url, Answers
from pages.main_page import HomePage, LogoYandex, OrderButten
from pages.dzen_page import LogoDzen
from pages.order_page import OrderPage


@allure.title('Проверка соответствия текстов для вопросов и ответов')
class TestHomePage:
    @pytest.mark.parametrize(
        'num, answer',
        [
            (0, Answers.answer_0),
            (1, Answers.answer_1),
            (2, Answers.answer_2),
            (3, Answers.answer_3),
            (4, Answers.answer_4),
            (5, Answers.answer_5),
            (6, Answers.answer_6),
            (7, Answers.answer_7)
        ]
    )
    @allure.title('Проверка соответствия текста ответа вопросу в разделе "Вопросы о важном"')
    def test_check_questions_and_answers(self, driver, num, answer):
        driver.get(Url.main_page)
        home_page = HomePage(driver)
        assert home_page.check_answer_text(num) == answer

@allure.title('Тестирование перехода по клику на логотип Яндекс')
class TestLogoDzen:
    @allure.title('Проверка перехода на "Дзен" по клику на лого "Яндекс"')
    def test_check_logo_yandex_open_dzen(self, driver):
        driver.get(Url.main_page)
        logo = LogoYandex(driver)
        dzen = LogoDzen(driver)
        logo.click_logo_yandex()
        logo.switch_to_new_window()
        assert dzen.check_dzen_logo().is_displayed()

@allure.title('Переход к оформлению заказа')
class TestOrderButten:
    @allure.title('Переход к форме для заказа с помощью кнопки "Заказать" вверху страницы')
    def test_check_button_to_order_top(self, driver):
        driver.get(Url.main_page)
        butten = OrderButten(driver)
        order = OrderPage(driver)
        butten.check_button_order_top()
        assert order.check_order_page_open().is_displayed()

    @allure.title('Переход к форме для заказа с помощью кнопки "Заказать" по центру страницы')
    def test_check_button_to_order_center(self, driver):
        driver.get(Url.main_page)
        butten = OrderButten(driver)
        order = OrderPage(driver)
        butten.check_button_to_order_center()
        assert order.check_order_page_open().is_displayed()
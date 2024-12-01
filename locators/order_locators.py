from selenium.webdriver.common.by import By

class OrderPageLocators:
    LOGO_SCOOTER = By.XPATH, "//*[@class='Header_LogoScooter__3lsAR']" # Логотип Самокат

class CookieBaLocator:
    BUTTON_COOKIE = By.ID, "rcc-confirm-button" # Кнопка "Да все привыкли", куки

class OrderForm1Locators:
    NAME = By.XPATH, "//input[@placeholder='* Имя']" # Поле ввода имени
    LAST_NAME = By.XPATH, "//input[@placeholder='* Фамилия']" # Поле ввода фамилии
    ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']" # Поле ввода адреса
    METRO = By.XPATH, "//input[@placeholder='* Станция метро']" # Поле выбора станции
    METRO_LUBANKA = By.XPATH, ".//*[contains(text(), 'Лубянка')]"  # Станция Лубянка
    METRO_SPORTIVNAY = By.XPATH, ".//*[contains(text(), 'Спортивная')]"  # Станция Спортивная
    PHONE = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']" # Поле ввода номера телефона
    NEXT = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']" # Кнопка далее

class OrderForm2Locators:
    TITLE_ABOUT_RENT = By.XPATH, "//*[@class='Order_Header__BZXOb']" # Заголовок формы заказа
    DATA_ORDER = By.XPATH, "//input[@placeholder='* Когда привезти самокат']" # Поле ввода даты доставки
    RENTAL_PERIOD = By.XPATH, "//*[@class='Dropdown-placeholder']" # Поле выбора продолжительности аренды
    RENT_1_DAY = By.XPATH, "//*[contains(text(), 'сутки')]" # Сутки аренды
    RENT_2_DAYS = By.XPATH, "//*[contains(text(), 'двое суток')]" # Двое суток аренды
    CHECKBOX_BLACK_COLOR = By.XPATH, "//*[contains(@id, 'black')]" # Выбор черного цвета
    CHECKBOX_GREY_COLOR = By.XPATH, "//*[contains(@id, 'grey')]" # Выбор серого цвета
    COMMENT_FOR_COURIER = By.XPATH, "//input[@placeholder='Комментарий для курьера']" # Поле ввода комментария
    BUTTON_TO_ORDER_IN_FORM = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']" # Кнопка заказать

class OrderPopUpLocators:
    BUTTON_YES_ORDER = By.XPATH, "//*[contains(text(), 'Да')]" # Кнопка да в окне "Хотите оформить заказ?"
    POP_UP_WINDOW_SUCCESSFUL_ORDER = By.XPATH, "//*[contains(text(), 'Заказ оформлен')]" # Информация о заказе
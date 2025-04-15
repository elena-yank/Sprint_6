from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Первая страница формы
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    PHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON_LOCATOR = (By.XPATH,
                           '//*[contains(@class, "Order_NextButton")]/*[contains(@class, "Button_Button")]')

    # Вторая страница формы
    DATE_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    DATE_PICKER = (By.XPATH, '//div[contains(@class, "react-datepicker")]')
    DATE_DAY = (By.XPATH, '//div[contains(@class, "react-datepicker__day") and not(contains(@class, "outside-month"))]')

    RENTAL_PERIOD_FIELD = (By.XPATH, '//div[contains(text(), "* Срок аренды")]')
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, '//div[@class="Dropdown-menu"]')
    RENTAL_PERIOD_OPTION = (By.XPATH, '//div[text()="двое суток"]')

    COLOR_BLACK = (By.XPATH, '//input[@id="black"]')

    ORDER_BUTTON_HEADER = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and text()="Заказать"]')
    ORDER_BUTTON_MIDDLE = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM")]')
    COMPLETE_ORDER = (By.XPATH,
                      '//button[contains(@class, "Button_Button__ra12g") and contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]')

    # Модальное окно подтверждения
    CONFIRMATION_MODAL = (By.XPATH, '//div[contains(text(), "Заказ оформлен")]')
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Да"]')




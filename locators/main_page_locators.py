from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_TEMPLATE = (By.XPATH, "//div[@id='accordion__heading-{0}']")
    ANSWER_TEMPLATE = (By.XPATH, "//div[@id='accordion__panel-{}']/p")

    FAQ_HEADER = (By.XPATH, "//div[contains(text(),'Вопросы о важном')]")

    # Кнопка заказа вверху страницы
    ORDER_BUTTON_HEADER = (By.XPATH, '//button[contains(@class, "Button_Button")]')
    # Кнопка заказа в середине страницы
    ORDER_BUTTON_MIDDLE = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and contains(@class, "Button_Middle__1CSJM")]')
    # Кнопки Яндекс и лого Скутера
    DZEN_BUTTON = (By.XPATH, '//img[@src="/assets/ya.svg" and @alt="Yandex"]')
    SAMOKAT_LOGO = (By.XPATH, '//img[@src="/assets/scooter.svg" and @alt="Scooter"]')

    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    COOKIE_POPUP = (By.XPATH, '//div[contains(@class, "App_CookieText__1sbqp")]')
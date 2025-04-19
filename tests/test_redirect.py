from data import URLs
from pages.main_page import MainPageSamokat
from locators.main_page_locators import MainPageLocators


class TestRedirects:
    def test_order_button_and_dzen_redirect(self, driver):
        main_page = MainPageSamokat(driver)

        # 1. Открываем главную страницу
        main_page.open(URLs.faq_main_page)

        # 2. Нажимаем верхнюю кнопку "Заказать"
        main_page.click(MainPageLocators.ORDER_BUTTON_HEADER)

        # 3. Нажимаем на Dzen и ждем
        main_page.click_dzen_and_wait()

        # 4. Проверяем URL
        assert any(domain in driver.current_url.lower() 
                 for domain in ['yandex.ru', 'dzen.ru'])

        # 5. Закрываем вкладку и возвращаемся
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_order_button_and_samokat_redirect(self, driver):
        main_page = MainPageSamokat(driver)

        # 1. Открываем главную страницу
        main_page.open(URLs.faq_main_page)

        # 2. Нажимаем верхнюю кнопку "Заказать"
        main_page.click(MainPageLocators.ORDER_BUTTON_HEADER)

        # 3. Нажимаем на логотип Самоката
        main_page.click(MainPageLocators.SAMOKAT_LOGO)

        # 4. Проверяем URL
        assert driver.current_url == URLs.faq_main_page_slash
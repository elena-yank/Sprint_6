from data import URLs
from pages.main_page import MainPageSamokat
from pages.redirect_page import RedirectPage

class TestRedirects:
    def test_order_button_and_dzen_redirect(self, driver):
        main_page = MainPageSamokat(driver)
        redirect_page = RedirectPage(driver)

        # 1. Открываем главную страницу
        main_page.open_url(URLs.faq_main_page)

        # 2. Нажимаем верхнюю кнопку "Заказать"
        main_page.click_order_button_header()

        # 3. Нажимаем на Dzen и ждем
        redirect_page.click_dzen_button()

        # 4. Проверяем URL
        redirect_page.is_redirected_to_dzen()


    def test_order_button_and_samokat_redirect(self, driver):
        main_page = MainPageSamokat(driver)
        redirect_page = RedirectPage(driver)

        # 1. Открываем главную страницу
        main_page.open_url(URLs.faq_main_page)

        # 2. Нажимаем верхнюю кнопку "Заказать"
        main_page.click_order_button_header()

        # 3. Нажимаем на логотип Самоката
        redirect_page.click_samokat_logo()

        # 4. Проверяем URL
        redirect_page.is_on_main_page()
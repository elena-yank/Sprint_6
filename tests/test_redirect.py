import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import URLs
from locators.main_page_locators import MainPageLocators


class TestRedirects:
    def test_order_button_and_dzen_redirect(self, driver):
        # 1. Открываем главную страницу
        driver.get(URLs.faq_main_page)

        # 2. Нажимаем верхнюю кнопку "Заказать"
        order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_HEADER)
        )
        order_button.click()

        # 3. Нажимаем на логотип Dzen (Яндекс)
        dzen_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.DZEN_BUTTON)
        )
        dzen_button.click()

        # 4. Проверяем переход на yandex.ru
        # Переключаемся на новую вкладку (Dzen открывается в новом окне)
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)
        driver.switch_to.window(driver.window_handles[1])

        # Ждем загрузки страницы и проверяем URL
        WebDriverWait(driver, 10).until(
            EC.url_contains("yandex.ru")
        )
        assert "yandex.ru" in driver.current_url.lower()

        # Закрываем вкладку Dzen и возвращаемся на исходную
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test_order_button_and_samokat_redirect(self, driver):
        # 1. Открываем главную страницу
        driver.get(URLs.faq_main_page)

        # 2. Нажимаем верхнюю кнопку "Заказать"
        order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_HEADER)
        )
        order_button.click()

        # 3. Нажимаем на логотип Dzen (Яндекс)
        samokat_logo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.SAMOKAT_LOGO)
        )
        samokat_logo.click()

        # 4. Проверяем переход на yandex.ru
        # Переключаемся на новую вкладку (Dzen открывается в новом окне)

        # Ждем загрузки страницы и проверяем URL
        WebDriverWait(driver, 10).until(
            EC.url_contains(URLs.faq_main_page_slash)
        )
        assert driver.current_url == URLs.faq_main_page_slash

        # Закрываем вкладку Dzen и возвращаемся на исходную
        driver.close()
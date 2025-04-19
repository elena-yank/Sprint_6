from datetime import datetime, timedelta
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure
import logging


class OrderPage(BasePage):
    @allure.step('Нажимаем сначала на верхнюю кнопку "Заказать", затем на нижнюю')
    def click_order_button(self, first=True):
        self.close_cookie_popup()  # Закрываем окно с куки, если оно есть

        if first:
            self.scroll_to_element(MainPageLocators.ORDER_BUTTON_HEADER)
            self.wait_for_clickable(MainPageLocators.ORDER_BUTTON_HEADER)
            self.click(MainPageLocators.ORDER_BUTTON_HEADER)
        else:
            self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MIDDLE)
            self.wait_for_clickable(MainPageLocators.ORDER_BUTTON_MIDDLE)
            self.click(MainPageLocators.ORDER_BUTTON_MIDDLE)

        self.wait_for_visible(OrderPageLocators.NAME_FIELD)

        # Ждем появления формы после нажатия на кнопку
        self.wait_for_visible(OrderPageLocators.NAME_FIELD)

    @allure.step('Заполняем форму "Для кого самокат"')
    def fill_user_info(self, name, surname, address, metro, phone):
        self.type(OrderPageLocators.NAME_FIELD, name)
        self.type(OrderPageLocators.SURNAME_FIELD, surname)
        self.type(OrderPageLocators.ADDRESS_FIELD, address)
        self.click(OrderPageLocators.METRO_FIELD)
        metro_option = (By.XPATH, f'//div[text()="{metro}"]')
        self.click(metro_option)
        self.type(OrderPageLocators.PHONE_FIELD, phone)
        self.click(OrderPageLocators.NEXT_BUTTON_LOCATOR)

    @allure.step('Выбираем дату через 2 дня от текущей, срок аренды, цвет')
    def fill_rent_info(self, color='black', comment=''):
        # Выбираем дату (через 2 дня от текущей)
        self.click(OrderPageLocators.DATE_FIELD)
        self.wait_for_visible(OrderPageLocators.DATE_PICKER)

        # Вычисляем дату через 2 дня
        target_date = datetime.now() + timedelta(days=2)
        day_xpath = f'//div[contains(@class, "react-datepicker__day") and not(contains(@class, "outside-month")) and text()="{target_date.day}"]'
        day_locator = (By.XPATH, day_xpath)
        self.click(day_locator)

        # Выбираем срок аренды
        self.click(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.wait_for_visible(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.RENTAL_PERIOD_OPTION)

        # Выбираем цвет
        self.click(OrderPageLocators.COLOR_BLACK)

    @allure.step('Нажимаем на кнопку "Далее"')
    def submit_order(self):
        self.wait_for_clickable(OrderPageLocators.NEXT_BUTTON_LOCATOR)
        self.click(OrderPageLocators.NEXT_BUTTON_LOCATOR)

    @allure.step('Нажимаем на кнопку "Заказать"')
    def complete_order(self):
        self.click(OrderPageLocators.COMPLETE_ORDER)

    @allure.step('Дожидаемся окна с сообщением об успешном завершении заказа')
    def confirm_order(self):
        try:
            self.click(OrderPageLocators.COMPLETE_ORDER)
            return self.wait_for_visible(OrderPageLocators.CONFIRMATION_MODAL)
        except TimeoutException as e:
            logging.warning(f"Вышло время ожидания окна подтверждения заказа: {e}")
        except NoSuchElementException as e:
            logging.warning(f"Не найдено окно подтверждения заказа: {e}")


    @allure.step('Скроллим до нужного элемента')
    def scroll_to_element(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.wait.until(EC.visibility_of(element))

    @allure.step('Ожидаем, пока элемент станет кликабельным')
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Закрываем окно с запросом на куки')
    def close_cookie_popup(self):
        cookie_button = (By.ID, 'rcc-confirm-button')
        try:
            if self.is_element_present(cookie_button):
                self.click(cookie_button)
        except (NoSuchElementException, TimeoutException) as e:
            logging.warning(f"Попап с куками не найден: {e}")



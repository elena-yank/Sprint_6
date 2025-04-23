from pages.base_page import BasePage
from data import TestDates
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure
import logging


class OrderPage(BasePage):

    @allure.step('Нажимаем сначала на верхнюю кнопку "Заказать", затем на нижнюю')
    def click_order_button(self, first=True):

        if first:
            self.scroll_to_element(MainPageLocators.ORDER_BUTTON_HEADER)
            self.wait_for_clickable(MainPageLocators.ORDER_BUTTON_HEADER)
            self.click(MainPageLocators.ORDER_BUTTON_HEADER)
        else:
            self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MIDDLE)
            self.wait_for_clickable(MainPageLocators.ORDER_BUTTON_MIDDLE)
            self.click(MainPageLocators.ORDER_BUTTON_MIDDLE)

        # Ждем появления формы после нажатия на кнопку
        self.wait_for_visible(OrderPageLocators.NAME_FIELD)

    @allure.step('Заполняем форму "Для кого самокат"')
    def fill_user_info(self, name, surname, address, phone):
        self.close_cookie_popup()
        self.type(OrderPageLocators.NAME_FIELD, name)
        self.type(OrderPageLocators.SURNAME_FIELD, surname)
        self.type(OrderPageLocators.ADDRESS_FIELD, address)
        self.click(OrderPageLocators.METRO_FIELD)
        self.click(OrderPageLocators.METRO_OPTION)
        self.type(OrderPageLocators.PHONE_FIELD, phone)
        self.click(OrderPageLocators.NEXT_BUTTON_LOCATOR)

    @allure.step('Выбираем дату через 2 дня от текущей, срок аренды, цвет')
    def fill_rent_info(self, color='black', comment='', days_offset=2):
        # Получаем дату
        future_date = TestDates.get_future_date(days_offset)

        # Формируем локатор дня
        day_locator = (
            OrderPageLocators.DAY_LOCATOR_TEMPLATE[0],
            OrderPageLocators.DAY_LOCATOR_TEMPLATE[1].format(future_date['day'])
        )

        # Выбираем дату
        self.click(OrderPageLocators.DATE_FIELD)
        self.wait_for_visible(OrderPageLocators.DATE_PICKER)
        self.scroll_to_element(day_locator)
        self.wait_for_clickable(day_locator)
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

    @allure.step('Проверяем отображение модального окна подтверждения создания заказа')
    def is_confirmation_modal_displayed(self):
        return self.is_element_present(OrderPageLocators.CONFIRMATION_MODAL)


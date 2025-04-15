import pytest
from selenium.webdriver.common.by import By
from data import URLs
from pages.order_page import OrderPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.parametrize("first_button, name, surname, address, metro, phone", [
    (True, "Кристина", "Трабл", "ул. Проблемная, 21", "Черкизовская", "89161234567"),
    (False, "Питер", "Проблемс", "ул. Арбат, 66", "Курская", "86666666666")
])
def test_order_creation(driver, first_button, name, surname, address, metro, phone):
    # Переходим на главную страницу
    driver.get(URLs.faq_main_page)

    order_page = OrderPage(driver)

    # 1. Нажимаем кнопку заказа
    order_page.click_order_button(first=first_button)

    # 2. Заполняем первую часть формы
    order_page.fill_user_info(name, surname, address, metro, phone)

    # 3. Заполняем вторую часть формы
    order_page.fill_rent_info()

    # 4. Заказываем
    order_page.complete_order()

    # 5. Отправляем заказ
    order_page.submit_order()

    # 6. Проверяем подтверждение заказа
    confirmation = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//div[contains(text(), "Заказ оформлен")]'))
    )
    assert confirmation.is_displayed()


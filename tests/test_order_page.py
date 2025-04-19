import pytest
from data import URLs, OrderTestData
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators

@pytest.mark.parametrize("order_data", OrderTestData.ORDER_DATA)
def test_order_creation(driver, order_data):
    # Переходим на главную страницу
    driver.get(URLs.faq_main_page)

    order_page = OrderPage(driver)

    # 1. Нажимаем кнопку заказа
    order_page.click_order_button(first=order_data["first_button"])

    # 2. Заполняем первую часть формы
    order_page.fill_user_info(
        order_data["name"],
        order_data["surname"],
        order_data["address"],
        order_data["metro"],
        order_data["phone"]
    )

    # 3. Заполняем вторую часть формы
    order_page.fill_rent_info()

    # 4. Заказываем
    order_page.complete_order()

    # 5. Отправляем заказ
    order_page.submit_order()

    # 6. Проверяем подтверждение заказа
    order_page.confirm_order()

    modal = driver.find_element(*OrderPageLocators.CONFIRMATION_MODAL)

    assert modal.is_displayed()


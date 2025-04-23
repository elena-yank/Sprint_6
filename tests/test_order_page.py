import pytest
from data import URLs, OrderTestData
from pages.order_page import OrderPage

class TestOrderCreation:
    @pytest.mark.parametrize("order_data", OrderTestData.ORDER_DATA)
    def test_order_creation(self, driver, order_data):
    # Переходим на главную страницу
        order_page = OrderPage(driver)
        order_page.open_url(URLs.faq_main_page)

    # 1. Нажимаем кнопку заказа
        order_page.click_order_button(first=order_data["first_button"])

    # 2. Заполняем первую часть формы
        order_page.fill_user_info(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
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

        assert order_page.is_confirmation_modal_displayed()


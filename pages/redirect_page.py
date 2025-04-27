import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import URLs

class RedirectPage(BasePage):
    @allure.step("Нажать на кнопку Яндекс")
    def click_dzen_button(self):
        self.click(MainPageLocators.DZEN_BUTTON)
        self.switch_to_new_tab()

    @allure.step("Нажать логотип Самоката")
    def click_samokat_logo(self):
        self.click(MainPageLocators.SAMOKAT_LOGO)

    @allure.step("Получить URL страницы в новом окне")
    def get_new_window_url(self):
        self.wait_and_switch_to_new_window()

    @allure.step("Проверяем, что мы перешли на главную страницу")
    def is_on_main_page(self):
        assert self.check_url_contains(URLs.faq_main_page_slash)

    @allure.step("Проверяем, что мы перешли на дзен")
    def is_redirected_to_dzen(self):
        assert self.check_url_contains(URLs.dzen_page)




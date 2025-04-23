import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

# класс главной страницы
class MainPageSamokat(BasePage):

    @allure.step("Открыть страницу")
    def open(self, url):
        self.open_url(url)

    @allure.step("Скроллим до вопросов и ответов")
    def scroll_to_faq_header(self):
        self.scroll_to_element(MainPageLocators.FAQ_HEADER)

    @allure.step("Подождать загрузки списка вопросов")
    def wait_for_questions_list(self):
        self.wait_for_visible(MainPageLocators.QUESTIONS)

    @allure.step("Открыть вопрос")
    def click_on_questions(self, question_number):
        question_locator = (MainPageLocators.QUESTION_TEMPLATE[0],
                            MainPageLocators.QUESTION_TEMPLATE[1].format(question_number))
        self.scroll_to_element(question_locator)
        self.click(question_locator)

    @allure.step("Сравнить текст вопроса")
    def check_questions_name(self, question_number, expected_text):
        question_locator = (MainPageLocators.QUESTION_TEMPLATE[0],
                            MainPageLocators.QUESTION_TEMPLATE[1].format(question_number))
        actual_text = self.get_text(question_locator)
        return actual_text == expected_text

    @allure.step("Получить текст ответа")
    def get_answer_text(self, answer_number):
        answer_locator = (MainPageLocators.ANSWER_TEMPLATE[0],
                          MainPageLocators.ANSWER_TEMPLATE[1].format(answer_number))
        return self.get_text(answer_locator)

    @allure.step("Проверить текст ответа")
    def check_answer_text(self, answer_number, expected_text):
        actual_text = self.get_answer_text(answer_number)
        return expected_text in actual_text

    @allure.step("Проверить вопрос и ответ")
    def check_question_and_answer(self, question_number, expected_question, expected_answer):
        assert self.check_questions_name(question_number, expected_question)
        self.click_on_questions(question_number)
        assert self.check_answer_text(question_number, expected_answer)

    @allure.step("Нажать на кнопку Яндекс")
    def click_dzen_button(self):
        self.click(MainPageLocators.DZEN_BUTTON)
        self.switch_to_new_tab()
        self.wait_for_url_contains('yandex.ru')

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_order_button_header(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Нажать логотип Самоката")
    def click_samokat_logo(self):
        self.click(MainPageLocators.SAMOKAT_LOGO)


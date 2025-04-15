import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

# класс главной страницы
class MainPageSamokat(BasePage):

    @allure.step("Скроллим до вопросо и ответов")
    def scroll_to_faq_header(self):
        # Прокрутка до элемента "Вопросы о важном"
        faq_header_element = self.driver.find_element(*MainPageLocators.FAQ_HEADER)
        actions = ActionChains(self.driver)
        actions.move_to_element(faq_header_element).perform()

    @allure.step("Подождать загрузки списка вопросов")
    def wait_for_questions_list(self):
        self.wait_for_element(MainPageLocators.QUESTIONS)

    @allure.step("Открыть вопрос")
    def click_on_questions(self, questions_number):
        card_locator = MainPageLocators.question_number(questions_number)
        self.scroll_to_element(card_locator)
        self.click_on_element(card_locator)

    @allure.step("Сравни текст вопроса")
    def check_questions_name(self, questions_number, expected_text):
        card_locator = MainPageLocators.question_text(questions_number)
        actual_text = self.get_text_on_element(card_locator)
        return actual_text == expected_text
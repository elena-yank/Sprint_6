import pytest
from pages.main_page import MainPageSamokat
from data import Answers, Questions, URLs
from locators.main_page_locators import MainPageLocators


class TestFAQQuestions:
    @pytest.mark.parametrize("index, question_text, expected_answer", [
        (0, Questions.FAQ_QUESTIONS[0], Answers.FAQ_ANSWERS[0]),
        (1, Questions.FAQ_QUESTIONS[1], Answers.FAQ_ANSWERS[1]),
        (2, Questions.FAQ_QUESTIONS[2], Answers.FAQ_ANSWERS[2]),
        (3, Questions.FAQ_QUESTIONS[3], Answers.FAQ_ANSWERS[3]),
        (4, Questions.FAQ_QUESTIONS[4], Answers.FAQ_ANSWERS[4]),
        (5, Questions.FAQ_QUESTIONS[5], Answers.FAQ_ANSWERS[5]),
        (6, Questions.FAQ_QUESTIONS[6], Answers.FAQ_ANSWERS[6]),
        (7, Questions.FAQ_QUESTIONS[7], Answers.FAQ_ANSWERS[7]),
    ])
    def test_faq_questions(self, driver, index, question_text, expected_answer):
        # Инициализация страницы
        page = MainPageSamokat(driver)

        # Открытие главной страницы
        page.open(URLs.faq_main_page)

        # Прокрутка до раздела FAQ
        page.scroll_to_faq_header()

        # Проверка текста вопроса
        assert page.check_questions_name(index, question_text)

        # Клик по вопросу
        page.click_on_questions(index)

        # Получение текста ответа
        answer_locator = (MainPageLocators.ANSWER_TEMPLATE[0],
                          MainPageLocators.ANSWER_TEMPLATE[1].format(index))
        actual_answer = page.get_text(answer_locator)

        # Проверка текста ответа
        assert expected_answer in actual_answer
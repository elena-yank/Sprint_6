import pytest
from pages.main_page import MainPageSamokat
from data import Answers, Questions, URLs


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
def test_faq_questions(driver, index, question_text, expected_answer):
    driver.get(URLs.faq_main_page)
    page = MainPageSamokat(driver)

    def test_faq_questions(driver, index, expected_answer):
        driver.get(URLs.faq_main_page)
        page = MainPageSamokat(driver)

        # Прокручиваем страницу до элемента "Вопросы о важном"
        page.scroll_to_faq_header()

        # Открываем вопрос и получаем ответ
        page.open_question(index)
        actual_answer = page.get_answer_text(index)

        # Проверяем, что ответ соответствует ожидаемому
        assert expected_answer in actual_answer

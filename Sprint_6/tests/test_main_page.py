import allure
from pages.main import MainPage
from tests.conftest import driver
from data import TestData
import pytest


class TestQuestionsAnswers:

    @allure.title('Проверяем формы ответов на "Вопросы о главном"')
    @pytest.mark.parametrize("number", list(range(8)))
    def test_check_answer_on_all_questions(self, driver, number):
        page = MainPage(driver)
        page.open_url(TestData.MAIN_URL)
        expected_answer = TestData.ANSWERS[number]
        actual_answer = page.check_question_and_answer(number)
        assert expected_answer == actual_answer

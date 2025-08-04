import allure
from pages.base import BasePage
from locators.main_locators import MainLocators


class MainPage(BasePage):

    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, locator): # метод скролл есть в base.py - здесь оформляем шаг теста
        return super().scroll_to_element(locator)

    @allure.step('Кликаем на вопрос')
    def click_on_question(self, number):
        clicked_locator = self.format_locator(MainLocators.QUESTION, number)
        self.scroll_to_element(MainLocators.SCROLL_TO_QUESTION)
        self.click_on_element(clicked_locator)

    @allure.step('Получаем ответ на вопрос')
    def get_answer_text(self, number):
        answer_locator = self.format_locator(MainLocators.ANSWER, number)
        return self.get_text(answer_locator)

    @allure.step('Проверяем ответ на вопрос')
    def check_question_and_answer(self, number):
        self.click_on_question(number)
        return self.get_answer_text(number)

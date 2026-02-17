import allure
from pages.base_page import BasePage


class FaqPage(BasePage):
    @allure.step("Открыть ответ на вопрос FAQ")
    def open_question(self, question_locator):
        self.click_with_scroll(question_locator)

    @allure.step("Получить текст ответа FAQ")
    def get_answer_text(self, answer_locator):
        return self.get_text_from_element(answer_locator)

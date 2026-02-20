import allure
from pages.base_page import BasePage
from locators.faq_page_locators import FaqLocators


class FaqPage(BasePage):

    @allure.step('Нажать на вопрос: "Сколько это стоит? И как оплатить?"')
    def click_price_question(self):
        self.click_with_scroll(FaqLocators.PRICE_QUESTION)

    @allure.step('Ответ на вопрос: "Сколько это стоит? И как оплатить?"')
    def get_price_answer(self):
        return self.get_text_from_element(FaqLocators.PRICE_ANSWER)

    @allure.step('Нажать на вопрос: "Хочу сразу несколько самокатов! Так можно?"')
    def click_quantity_question(self):
        self.click_with_scroll(FaqLocators.QUANTITY_QUESTION)

    @allure.step('Ответ на вопрос: "Хочу сразу несколько самокатов! Так можно?"')
    def get_quantity_answer(self):
        return self.get_text_from_element(FaqLocators.QUANTITY_ANSWER)

    @allure.step('Нажать на вопрос: "Как рассчитывается время аренды?"')
    def click_rent_time_question(self):
        self.click_with_scroll(FaqLocators.RENT_TIME_QUESTION)

    @allure.step('Ответ на вопрос: "Как рассчитывается время аренды?"')
    def get_rent_time_answer(self):
        return self.get_text_from_element(FaqLocators.RENT_TIME_ANSWER)

    @allure.step('Нажать на вопрос: "Можно ли заказать самокат прямо на сегодня?"')
    def click_today_order_question(self):
        self.click_with_scroll(FaqLocators.TODAY_ORDER_QUESTION)

    @allure.step('Ответ на вопрос: "Можно ли заказать самокат прямо на сегодня?"')
    def get_today_order_answer(self):
        return self.get_text_from_element(FaqLocators.TODAY_ORDER_ANSWER)

    @allure.step(
        'Нажать на вопрос: "Можно ли продлить заказ или вернуть самокат раньше?"'
    )
    def click_return_or_extend_question(self):
        self.click_with_scroll(FaqLocators.RETURN_OR_EXTEND_QUESTION)

    @allure.step(
        'Ответ на вопрос: "Можно ли продлить заказ или вернуть самокат раньше?"'
    )
    def get_return_or_extend_answer(self):
        return self.get_text_from_element(FaqLocators.RETURN_OR_EXTEND_ANSWER)

    @allure.step('Нажать на вопрос: "Вы привозите зарядку вместе с самокатом?"')
    def click_charger_delivery_question(self):
        self.click_with_scroll(FaqLocators.CHARGER_DELIVERY_QUESTION)

    @allure.step('Ответ на вопрос: "Вы привозите зарядку вместе с самокатом?"')
    def get_charger_delivery_answer(self):
        return self.get_text_from_element(FaqLocators.CHARGER_DELIVERY_ANSWER)

    @allure.step('Нажать на вопрос: "Можно ли отменить заказ?"')
    def click_order_cancellation_question(self):
        self.click_with_scroll(FaqLocators.ORDER_CANCELLATION_QUESTION)

    @allure.step('Ответ на вопрос: "Можно ли отменить заказ?"')
    def get_order_cancellation_answer(self):
        return self.get_text_from_element(FaqLocators.ORDER_CANCELLATION_ANSWER)

    @allure.step('Нажать на вопрос: "Я живу за МКАДом, привезёте?"')
    def click_order_area_question(self):
        self.click_with_scroll(FaqLocators.ORDER_AREA_QUESTION)

    @allure.step('Ответ на вопрос: "Я живу за МКАДом, привезёте?"')
    def get_order_area_answer(self):
        return self.get_text_from_element(FaqLocators.ORDER_AREA_ANSWER)

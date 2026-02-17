import allure


from pages.faq_page import FaqPage
from utils.faq_test_data import FAQ_DATA


class TestFaq:

    @allure.title('Проверка FAQ: "Сколько это стоит? И как оплатить?"')
    def test_price_question(self, driver):
        self._check_faq_answer(driver, 0)

    @allure.title('Проверка FAQ: "Хочу сразу несколько самокатов! Так можно?"')
    def test_quantity_question(self, driver):
        self._check_faq_answer(driver, 1)

    @allure.title('Проверка FAQ: "Как рассчитывается время аренды?"')
    def test_rent_time_question(self, driver):
        self._check_faq_answer(driver, 2)

    @allure.title('Проверка FAQ: "Можно ли заказать самокат прямо на сегодня?"')
    def test_today_order_question(self, driver):
        self._check_faq_answer(driver, 3)

    @allure.title('Проверка FAQ: "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_return_or_extend_question(self, driver):
        self._check_faq_answer(driver, 4)

    @allure.title('Проверка FAQ: "Вы привозите зарядку вместе с самокатом?"')
    def test_charger_delivery_question(self, driver):
        self._check_faq_answer(driver, 5)

    @allure.title('Проверка FAQ: "Можно ли отменить заказ?"')
    def test_order_cancellation_question(self, driver):
        self._check_faq_answer(driver, 6)

    @allure.title('Проверка FAQ: "Я живу за МКАДом, привезёте?"')
    def test_order_area_question(self, driver):
        self._check_faq_answer(driver, 7)

    def _check_faq_answer(self, driver, index):
        page = FaqPage(driver)

        question_locator, answer_locator, expected_text = FAQ_DATA[index]

        page.open_question(question_locator)
        actual_text = page.get_answer_text(answer_locator)

        assert actual_text.strip() == expected_text.strip()

import allure


from pages.faq_page import FaqPage


class TestFaq:

    @allure.title('Проверка FAQ: "Сколько это стоит? И как оплатить?"')
    def test_price_faq(self, driver):
        page = FaqPage(driver)
        page.click_price_question()
        text = page.get_price_answer()
        assert "Сутки — 400 рублей. Оплата курьеру — наличными или картой." in text

    @allure.title('Проверка FAQ: "Хочу сразу несколько самокатов! Так можно?"')
    def test_order_few_faq(self, driver):
        page = FaqPage(driver)
        page.click_quantity_question()
        text = page.get_quantity_answer()
        assert (
            "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
            in text
        )

    @allure.title('Проверка FAQ: "Как рассчитывается время аренды?"')
    def test_time_rent_faq(self, driver):
        page = FaqPage(driver)
        page.click_rent_time_question()
        text = page.get_rent_time_answer()
        assert (
            "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
            in text
        )

    @allure.title('Проверка FAQ: "Можно ли заказать самокат прямо на сегодня?"')
    def test_order_today_faq(self, driver):
        page = FaqPage(driver)
        page.click_today_order_question()
        text = page.get_today_order_answer()
        assert "Только начиная с завтрашнего дня. Но скоро станем расторопнее." in text

    @allure.title('Проверка FAQ: "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_extend_or_return_faq(self, driver):
        page = FaqPage(driver)
        page.click_return_or_extend_question()
        text = page.get_return_or_extend_answer()
        assert (
            "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
            in text
        )

    @allure.title('Проверка FAQ: "Вы привозите зарядку вместе с самокатом?"')
    def test_scooter_charger_faq(self, driver):
        page = FaqPage(driver)
        page.click_charger_delivery_question()
        text = page.get_charger_delivery_answer()
        assert (
            "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
            in text
        )

    @allure.title('Проверка FAQ: "Можно ли отменить заказ?"')
    def test_cancel_order_faq(self, driver):
        page = FaqPage(driver)
        page.click_order_cancellation_question()
        text = page.get_order_cancellation_answer()
        assert (
            "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
            in text
        )

    @allure.title('Проверка FAQ: "Я жизу за МКАДом, привезёте?"')
    def test_outside_mkad_faq(self, driver):
        page = FaqPage(driver)
        page.click_order_area_question()
        text = page.get_order_area_answer()
        assert (
            "Да, обязательно. Всем самокатов! И Москве, и Московской области." in text
        )

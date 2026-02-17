import allure
import pytest


from pages.order_page import OrderPage
from utils.order_test_data import ORDER_TEST_DATA
from utils.urls import BASE_URL, ORDER_URL


class TestOrder:
    @allure.title("Проверка заказа через верхнюю кнопку Заказать на главной странице")
    @pytest.mark.parametrize("data", ORDER_TEST_DATA)
    def test_order_from_header_button(self, driver, data):
        page = OrderPage(driver)
        page.click_on_header_order_button()
        page.order_form(
            data["name"],
            data["last_name"],
            data["address"],
            data["station"],
            data["phone"],
        )
        page.about_order_form(data["period"], data["color"], data["comment"])
        assert page.is_success_status_displayed()

    @allure.title("Проверка заказа через нижнюю кнопку Заказать на главной странице")
    @pytest.mark.parametrize("data", ORDER_TEST_DATA)
    def test_order_from_bottom_button(self, driver, data):
        page = OrderPage(driver)
        page.click_on_bottom_order_button()
        page.order_form(
            data["name"],
            data["last_name"],
            data["address"],
            data["station"],
            data["phone"],
        )
        page.about_order_form(data["period"], data["color"], data["comment"])
        assert page.is_success_status_displayed()

    @allure.title(
        "Проверка перехода на главную страницу сервиса через логотип Самоката"
    )
    def test_scooter_logo(self, driver):
        page = OrderPage(driver)
        driver.get(BASE_URL + ORDER_URL)
        page.click_on_scooter_logo()
        assert BASE_URL in driver.current_url

    @allure.title(
        'Проверка перехода на главную страницу "Дзен" при нажатии на логотип Яндекса'
    )
    def test_ya_logo(self, driver):
        page = OrderPage(driver)
        page.click_on_ya_logo()
        page.wait_url_contains("dzen.ru")
        assert page.is_url_contains("dzen.ru")

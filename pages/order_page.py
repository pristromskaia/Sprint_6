import allure

from pages.base_page import BasePage
from locators.order_page_locators import (
    OrderButtonLocators,
    OrderFormLocators,
    AboutRentLocators,
    OrderLogo,
)


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Кликнуть на верхнюю кнопку заказать")
    def click_on_header_order_button(self):
        self.click_with_scroll(OrderButtonLocators.ORDER_BUTTON_TOP)

    @allure.step("Кликнуть на нижнюю кнопку заказать")
    def click_on_bottom_order_button(self):
        self.click_with_scroll(OrderButtonLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Выбрать станцию метро")
    def select_subway_station(self, station):
        subway_element = self.wait_for_element_clickable(OrderFormLocators.SUBWAY_FIELD)
        subway_element.click()
        subway_element.send_keys(station)
        self.wait_for_element_clickable(
            OrderFormLocators.SUBWAY_STATION_DROPDOWN
        ).click()

    @allure.step('Заполнить форму заказа: "Для кого самокат"')
    def order_form(self, name, last_name, address, station, phone):
        self.wait_for_element_visible(OrderFormLocators.ORDER_TITLE)
        self.enter_text(OrderFormLocators.NAME_FIELD, name)
        self.enter_text(OrderFormLocators.LAST_NAME_FIELD, last_name)
        self.enter_text(OrderFormLocators.ADDRESS_FIELD, address)
        self.select_subway_station(station)
        self.enter_text(OrderFormLocators.PHONE_FIELD, phone)
        self.click_with_scroll(OrderFormLocators.NEXT_BUTTON)

    @allure.step("Выбрать дату доставки")
    def select_order_date(self):
        self.wait_for_element_clickable(AboutRentLocators.ORDER_DATE_FIELD)
        self.click_with_scroll(AboutRentLocators.ORDER_DATE_FIELD)
        self.click_with_scroll(AboutRentLocators.ORDER_DATE_SELECT_DAY)

    @allure.step("Выбрать период аренды")
    def select_scooter_period(self, period):
        control = self.wait_for_element_visible(AboutRentLocators.RENT_PERIOD)
        self.scroll_to_element(control)
        self.action_click(control)
        self.wait_for_element_visible(AboutRentLocators.RENT_PERIOD_MENU)
        period_locator = {
            "сутки": AboutRentLocators.RENT_PERIOD_ONE_DAY,
            "семеро суток": AboutRentLocators.RENT_PERIOD_SEVEN_DAYS,
        }
        option = self.wait_for_element_visible(period_locator[period])
        self.scroll_to_element(option)
        self.action_click(option)

    @allure.step("Выбрать цвет самоката")
    def select_scooter_color(self, color):
        self.wait_for_element_clickable(AboutRentLocators.SCOOTER_COLOR_GREY)
        color_locator = {
            "black": AboutRentLocators.SCOOTER_COLOR_BLACK,
            "grey": AboutRentLocators.SCOOTER_COLOR_GREY,
        }
        locator = color_locator[color]
        self.click_with_scroll(locator)

    @allure.step('Заполнить форму заказа: "Про аренду"')
    def about_order_form(self, period, color, comment):
        self.wait_for_element_visible(AboutRentLocators.RENT_TITLE)
        self.select_order_date()
        self.select_scooter_period(period)
        self.select_scooter_color(color)
        self.enter_text(AboutRentLocators.COMMENT_FIELD, comment)
        self.click_with_scroll(AboutRentLocators.ORDER_BUTTON)
        self.wait_for_element_visible(AboutRentLocators.CONFIRM_BUTTON)
        self.click_with_scroll(AboutRentLocators.CONFIRM_BUTTON)

    @allure.step("Получить информацию об успешном заказе")
    def is_success_status_displayed(self):
        return self.wait_for_element_visible(AboutRentLocators.SUCCESS_ORDER)

    @allure.step("Нажать на логотип Яндекса")
    def click_on_ya_logo(self):
        self.click_with_scroll(OrderLogo.YANDEX_LOGO)
        self.switch_to_new_window()

    @allure.step('Нажать на логотип "Самокат"')
    def click_on_scooter_logo(self):
        self.click_with_scroll(OrderLogo.SCOOTER_LOGO)

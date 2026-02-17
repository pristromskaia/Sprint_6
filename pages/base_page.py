import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

from utils.waiter import DEFAULT_WAIT_TIME


class BasePage:
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_WAIT_TIME)

    @allure.step("Ожидание видимости")
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание клибельности элемента")
    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, element):
        self.driver.execute_script(
            'arguments[0].scrollIntoView({block: "center"});', element
        )

    @allure.step("Ожидание, скролл и клик по элементу")
    def click_with_scroll(self, locator):
        element = self.wait_for_element_clickable(locator)
        self.scroll_to_element(element)
        self.click_on_element(element)

    @allure.step("Клик по элементу с помощью ActionChains")
    def action_click(self, element):
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    @allure.step("Клик по элементу")
    def click_on_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидание, что URL содержит нужный текст")
    def wait_url_contains(self, text):
        self.wait.until(EC.url_contains(text))

    @allure.step("Получение текста")
    def get_text_from_element(self, locator):
        element = self.wait_for_element_visible(locator)
        return element.text

    @allure.step("Ввод текста")
    def enter_text(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.send_keys(text)

    @allure.step("Получение URL")
    def is_url_contains(self, text):
        return text in self.driver.current_url

    @allure.step("Переход на новое окно")
    def switch_to_new_window(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

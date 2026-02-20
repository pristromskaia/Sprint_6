import pytest
from selenium import webdriver

from utils.urls import BASE_URL


# Фикстура для инициализации сайта
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

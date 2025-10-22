import allure
import pytest
from selenium import webdriver
from data import BASE_URL
from pages.main import MainPage
from pages.get_taxi import GetTaxiPage


@allure.title("Открываем главную страницу Яндекс Маршруты")
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Открываем главную страницу и вводим два адреса")
@pytest.fixture
def driver_with_addresses(driver):
    page = MainPage(driver)
    page.input_addresses()
    return driver

@allure.title("Открываем окно выбора тарифа такси для тарифа Быстрый")
@pytest.fixture
def driver_and_choose_fast_taxi(driver_with_addresses):
    page = MainPage(driver_with_addresses)
    page.call_fast_taxi_route()
    return driver_with_addresses

@allure.title("Открываем окно поиска такси (тариф Рабочий + столик для ноутбука)")
@pytest.fixture
def driver_and_order_taxi(driver_and_choose_fast_taxi):
    page = GetTaxiPage(driver_and_choose_fast_taxi)
    page.click_tariff('work')  # Нажимаем на тариф Рабочий
    page.click_on_extra_wishes_title()  # Раскрываем блок с требованиями к заказу
    page.scroll_down_extra_panel()  # Прокручиваем вниз панель с доп. опциями
    page.click_on_extra_info_laptop_checkbox()  # Нажимаем на чекбокс 'Столик для ноутбука'
    page.click_on_extra_info_get_taxi_button()  # Нажимаем на кнопку 'Ввести номер и заказать'
    return driver_and_choose_fast_taxi

import allure
from pages.order import OrderPage
from tests.conftest import driver
from data import TestData
import pytest


class TestOrderPage:

    @allure.title('Проверяем работу верхней кнопки  "Заказать"')
    def test_open_top_button(self, driver): # Проверяем верхнюю кнопку Заказать
        page = OrderPage(driver)
        page.open_url(TestData.MAIN_URL)
        page.click_top_button()
        title = page.get_text_title()
        assert "Для кого самокат" in title

    @allure.title('Проверяем работу нижней кнопки  "Заказать"')
    def test_open_bottom_button(self, driver):  # Проверяем нижнюю кнопку Заказать
        page = OrderPage(driver)
        page.open_url(TestData.MAIN_URL)
        page.click_bottom_button()
        title = page.get_text_title()
        assert "Для кого самокат" in title

    @allure.title('Проверяем процедуру заказа самоката')
    @pytest.mark.parametrize('user', [TestData.ORDER_USER_1, TestData.ORDER_USER_2])
    def test_order_a_scooter(self, driver, user):
        page = OrderPage(driver)
        page.open_url(TestData.MAIN_URL)
        page.click_top_button()

        page.fill_user_data(user)
        page.fill_order_details(user)

        page.order_scooter()
        status = page.check_scooter_status()

        assert "Заказ оформлен" in status

import allure
from pages.base import BasePage
from locators.header_locators import HeaderLocators
from data import TestData


class Header(BasePage):
    @allure.step('Проверяем открытие главной страницы Самоката')
    def check_home_page_opened(self):
        return TestData.SCOOTER_TEXT in self.driver.page_source

    @allure.step('Нажимаем на логотип Самоката')
    def click_scooter_logo(self):
        self.click_on_element(HeaderLocators.LOGO_SCOOTER)

    @allure.step('Нажимаем на логотип Яндекс')
    def click_yandex_logo(self):
        self.click_on_element(HeaderLocators.LOGO_YANDEX)

    @allure.step('Проверяем открытие Дзена')
    def check_dzen_page_opened(self):
        return TestData.DZEN_URL in self.get_current_url()

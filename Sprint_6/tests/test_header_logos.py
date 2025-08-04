import allure
from pages.main import MainPage
from pages.header import Header
from data import TestData


class TestHeaderLinks:

    @allure.title('Проверяем что при нажатии на логотип «Самоката» открывается главная страница сервиса')
    def test_scooter_logo_go_home(self, driver):
        page = MainPage(driver)
        page.open_url(TestData.MAIN_URL)

        header = Header(driver)
        header.click_scooter_logo()

        assert header.check_home_page_opened()

    @allure.title('Проверяем, что при нажатии на логотип Яндекса в новой вкладке откроется главная страница Дзена')
    def test_yandex_logo_goes_to_dzen(self, driver):
        page = MainPage(driver)
        page.open_url(TestData.MAIN_URL)

        header = Header(driver)
        header.click_yandex_logo()

        header.switch_to_new_tab()

        assert header.check_dzen_page_opened()

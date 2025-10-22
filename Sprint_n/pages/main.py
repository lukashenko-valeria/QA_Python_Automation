from pages.base import BasePage
from  locators.main_page_locators import MainLocators
from data import ADDRESS_ONE, ADDRESS_TWO
import allure


class MainPage(BasePage):
    @allure.step("Вводим адрес в поле Откуда")
    def input_start_address(self, address):
        self.input_text(MainLocators.FROM_LOCATOR, address)

    @allure.step("Вводим адрес в поле Куда")
    def input_end_address(self, address):
        self.input_text(MainLocators.END_LOCATOR, address)

    @allure.step("Получаем список точек маршрута на карте")
    def get_list_of_travel_points(self):
        return self.get_list_of_elements(MainLocators.POINTS)

    @allure.step("Вводим адрес в поля Откуда и Куда")
    def input_addresses(self):
        self.input_text(MainLocators.FROM_LOCATOR, ADDRESS_ONE)
        self.input_text(MainLocators.END_LOCATOR, ADDRESS_TWO)

    @allure.step("Проверяем появление панели выбора маршрута")
    def visibility_of_route_panel(self):
        return self.find_element_with_visibility_wait(MainLocators.ROUTE_PANEL)

    @allure.step("Переключаемся по вкладкам маршрута")
    def click_route(self, locator):
        self.find_element_with_visibility_wait(locator)
        self.click_on_element(locator)

    @allure.step("Получаем список вкладок с вариантами маршрутов")
    def get_routes_tabs(self):
        tabs = self.get_list_of_elements(MainLocators.ROUTE_TAB)
        return tabs

    @allure.step("Нажимаем на вкладку 'Оптимальный'")
    def click_on_optimal_tab(self):
        tab = self.get_routes_tabs()[0]
        self.click_on_element_without_locator(tab)

    @allure.step("Нажимаем на вкладку 'Быстрый'")
    def click_on_fast_tab(self):
        tab = self.get_routes_tabs()[1]
        self.click_on_element_without_locator(tab)

    @allure.step("Получаем текст вкладки по индексу")
    def get_tab_text_by_index(self, index):
        tab = self.get_routes_tabs()[index]
        return tab.text

    @allure.step("Получаем текст вкладки 'Быстрый'")
    def get_fast_tab_text(self):
        return self.get_tab_text_by_index(1)

    @allure.step("Получаем текст вкладки 'Оптимальный'")
    def get_optimal_tab_text(self):
        return self.get_tab_text_by_index(0)

    @allure.step("Получаем текст вкладки 'Свой'")
    def get_own_tab_text(self):
        return self.get_tab_text_by_index(2)

    @allure.step("Получаем текст со стоимостью поездки")
    def get_text_from_price_description(self):
        return self.get_text_by_locator(MainLocators.TEXT_CAR)

    @allure.step("Проверяем активность опции 'Авто'")
    def car_option_activity(self):
        return self.find_element_with_visibility_wait(MainLocators.CAR_OPTION)

    @allure.step("Проверяем активность опции 'Пешком'")
    def walk_option_activity(self):
        return self.find_element_with_visibility_wait(MainLocators.WALK_OPTION)

    @allure.step("Проверяем активность опции 'Такси'")
    def taxi_option_activity(self):
        return self.find_element_with_visibility_wait(MainLocators.TAXI_OPTION)

    @allure.step("Проверяем активность опции 'Велосипед'")
    def bike_option_activity(self):
        return self.find_element_with_visibility_wait(MainLocators.TAXI_OPTION)

    @allure.step("Проверяем активность опции 'Самокат'")
    def scooter_option_activity(self):
        return self.find_element_with_visibility_wait(MainLocators.SCOOTER_OPTION)

    @allure.step("Проверяем активность опции 'Драйв'")
    def drive_option_activity(self):
        return self.find_element_with_visibility_wait(MainLocators.DRIVE_OPTION)

    @allure.step("Проверяем активность опций Авто, Пешком, Такси, Велосипед")
    def all_options_activity(self):
        return (self.car_option_activity() and
                self.walk_option_activity() and
                self.taxi_option_activity() and
                self.bike_option_activity() and
                self.scooter_option_activity() and
                self.drive_option_activity())

    @allure.step("Заказываем такси с вкладки Быстрый")
    def call_fast_taxi_route(self):
        self.click_route(MainLocators.FAST)
        self.click_on_element(MainLocators.BUTTON_CALL_TAXI)

    @allure.step("Заказываем с вкладки Свой, Драйв")
    def call_own_taxi_route(self):
        self.click_route(MainLocators.OWN)
        self.click_on_element(MainLocators.DRIVE_OPTION)

    @allure.step("Получаем текст кнопки Забронировать")
    def get_book_button_text(self):
        return self.get_text_by_locator(MainLocators.BUTTON_BOOK_CAR)

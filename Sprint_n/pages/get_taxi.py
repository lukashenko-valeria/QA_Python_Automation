from pages.base import BasePage
from  locators.get_taxi_locators import GetTaxiLocators
from data import TARIFF_LIST
import  allure
from selenium.webdriver.common.by import By


class GetTaxiPage(BasePage):

    @allure.step("Получаем список всех отображающихся тарифов")
    def get_list_of_tariff_names(self):
        tariff_list = self.get_list_of_elements(GetTaxiLocators.TAXI_TARIFFS)
        return [self.get_text(tariff) for tariff in tariff_list]

    @allure.step("Получаем название активного тарифа")
    def get_active_tariff_name(self, locator):
        return self.get_text_by_locator(locator)

    @allure.step("Проверяем, что в списке тарифов есть активный тариф")
    def tariff_active_in_tariff_list(self):
        active_tariff = self.get_active_tariff_name(GetTaxiLocators.TAXI_TARIFFS)
        all_tariffs = self.get_list_of_tariff_names()
        return active_tariff in all_tariffs

    @allure.step("Проверяем, все ли ожидаемые тарифы отображаются в списке тарифов")
    def expected_tariff_in_list_of_tariff_names(self):
        tariff_list = self.get_list_of_tariff_names()
        for tariff in TARIFF_LIST :
            if tariff in tariff_list:
                continue
            else:
                return False
        return True

    @allure.step("Наводим курсор на иконку i")
    def focus_on_info_icon(self, locator):
        self.focus_on_element(locator)

    @allure.step("Проверяем, что отображается окно с подсказкой")
    def is_info_panel_visible(self):
        return self.element_is_visible(GetTaxiLocators.ACTIVE_DESCRIPTION)

    @allure.step("Заголовок окна с подсказкой")
    def get_info_panel_title(self):
        return self.get_text_by_locator(GetTaxiLocators.ACTIVE_TITLE)

    @allure.step("Описание окна с подсказкой")
    def get_info_panel_description(self):
        return self.get_text_by_locator(GetTaxiLocators.ACTIVE_DESCRIPTION)

    @allure.step("Кликаем на тариф {tariff_name}")
    def click_tariff(self, tariff_name):
        # Словарь для соответствия английских имен русским названиям
        name_mapping = {
            'work': 'Рабочий',
            'sleep': 'Сонный',
            'holiday': 'Отпускной',
            'talk': 'Разговорчивый',
            'glad': 'Утешительный',
            'glam': 'Глянцевый'
        }

        russian_name = name_mapping.get(tariff_name)
        tariff_locator = (By.XPATH, f".//div[contains(@class, 'tcard') and .//div[text()='{russian_name}']]")
        self.click_on_element(tariff_locator)

    @allure.step("Получаем текст поля Телефон")
    def get_phone_field_text(self):
        return self.get_text_by_locator(GetTaxiLocators.TEXT_PHONE_FIELD)

    @allure.step("Получаем текст поля Способ оплаты")
    def get_payment_field_text(self):
        return self.get_text_by_locator(GetTaxiLocators.TEXT_PAYMENT_INFO)

    @allure.step("Получаем текст поля Комментарий водителю")
    def get_comment_field_text(self):
        return self.get_text_by_locator(GetTaxiLocators.TEXT_COMMENT_FIELD)

    @allure.step("Получаем заголовок блока Требования к заказу")
    def get_requirements_field_text(self):
        return self.get_text_by_locator(GetTaxiLocators.TEXT_REQUIREMENTS)

    @allure.step("Получаем текст кнопки Заказать такси")
    def get_order_taxi_button_text(self):
        return self.get_text_by_locator(GetTaxiLocators.TEXT_GET_TAXI_BUTTON)

    @allure.step("Раскрываем блок с требованиями к заказу")
    def click_on_extra_wishes_title(self):
        self.click_on_element(GetTaxiLocators.TEXT_EXTRA_WISHES_REQS_ARROW)

    @allure.step("Прокручиваем вниз панель с доп. опциями")
    def scroll_down_extra_panel(self):
        extra_info_panel = self.find_element_with_clickable(GetTaxiLocators.EXTRA_INFO_PANEL)
        self.move_down_in_container(extra_info_panel)

    @allure.step("Нажимаем на чекбокс Столик для ноутбука")
    def click_on_extra_info_laptop_checkbox(self):
        self.find_element_with_clickable(GetTaxiLocators.EXTRA_INFO_LAPTOP_CHECKBOX)
        self.click_on_element(GetTaxiLocators.EXTRA_INFO_LAPTOP_CHECKBOX)

    @allure.step("Нажимаем на кнопку Заказать такси")
    def click_on_extra_info_get_taxi_button(self):
        self.click_on_element(GetTaxiLocators.TEXT_GET_TAXI_BUTTON)


import pytest
from pages.get_taxi import GetTaxiPage
from locators.get_taxi_locators import GetTaxiLocators
import allure
from tests.conftest import driver_and_choose_fast_taxi
from data import TariffText, ExtraPanelText


@allure.suite("Тесты заказа тарифа такси")
class TestGetTaxi:

    @allure.description("Проверяем, что в списке тарифов есть тарифы по ТЗ")
    def test_get_taxi_activity_tariff(self, driver_and_choose_fast_taxi):  # Задание 4. Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный
        page = GetTaxiPage(driver_and_choose_fast_taxi)
        tariff_names = page.get_list_of_tariff_names()

        assert len(tariff_names) > 0
        assert page.expected_tariff_in_list_of_tariff_names()

    @allure.title("Проверяем появление кнопки Ввести номер и заказать при выборе тарифа Быстрый")
    def test_call_taxi_activity_fast_route(self, driver_and_choose_fast_taxi):  # Задание 4.
        page = GetTaxiPage(driver_and_choose_fast_taxi)
        button = page.get_text_by_locator(GetTaxiLocators.BUTTON_CALL_NUMBER) # можно вынести в отдельный метод эту строку  и следующую
        tariff_name = page.get_active_tariff_name(GetTaxiLocators.TAXI_TARIFFS)

        assert 'Ввести номер и заказать' in button
        assert 'Рабочий' in tariff_name

    @allure.title("В списке тарифов по умолчанию один тариф - активный")
    def test_tariffs_list_include_active_tariff(self, driver_and_choose_fast_taxi):
        page = GetTaxiPage(driver_and_choose_fast_taxi)

        assert page.tariff_active_in_tariff_list()

    @allure.title("При наведении на i отображается подсказка с информацией о тарифе")
    def test_focus_on_info_button_shows_info_panel(self, driver_and_choose_fast_taxi): # При наведении на иконку i в правом верхнем углу каждого тарифа отображается всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ
        page = GetTaxiPage(driver_and_choose_fast_taxi)
        page.focus_on_info_icon(GetTaxiLocators.INFO_BUTTON_I)

        assert page.is_info_panel_visible()

    @allure.title("Проверяем карточки с информацией для всех тарифов такси на соответствие ТЗ")
    @pytest.mark.xfail(reason="описания тарифов Разговорчивый и Сонный перепутаны местами")
    @pytest.mark.parametrize('tariff_name, expected_texts', [
        ('work', TariffText.WORK),
        ('sleep', TariffText.SLEEP),
        ('holiday', TariffText.HOLIDAY),
        ('talk', TariffText.TALK),
        ('glad', TariffText.GLAD),
        ('glam', TariffText.GLAM)])
    def test_title_and_description_info_panel_with_expected_texts(self, driver_and_choose_fast_taxi, tariff_name, expected_texts):
        page = GetTaxiPage(driver_and_choose_fast_taxi)
        page.click_tariff(tariff_name)

        page.focus_on_info_icon(GetTaxiLocators.INFO_BUTTON_I)
        actual_title = page.get_info_panel_title() # Получаем тексты из информационной панели
        actual_description = page.get_info_panel_description()

        assert actual_title == expected_texts['title']  # Проверяем соответствие ожидаемым значениям
        assert actual_description == expected_texts['description']

    @allure.title("Проверяем, что все поля блока дополнительной информации присутствуют и заголовки соответствуют ТЗ")
    def test_extra_info_panel_include_phone_payment_comment_and_extra_wishes_fields(self, driver_and_choose_fast_taxi):
        page = GetTaxiPage(driver_and_choose_fast_taxi)
        assert (page.get_phone_field_text() == ExtraPanelText.PHONE and
                page.get_payment_field_text() == ExtraPanelText.PAY_METHOD and
                page.get_comment_field_text() == ExtraPanelText.COMMENT and
                page.get_requirements_field_text() == ExtraPanelText.REQS and
                page.get_order_taxi_button_text() == ExtraPanelText.ORDER)

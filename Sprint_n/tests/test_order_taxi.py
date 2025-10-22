from pages.order_taxi import OrderTaxiPage
from data import WaitTaxiText
import allure
import pytest


@allure.suite("Тесты вызова такси и ожидания поиска машины")
class TestOrderTaxi:
    @allure.title("Нажатие на кнопку Заказать такси открывает окно ожидания машины")
    @allure.description(
        "Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать")
    def test_click_on_extra_info_order_taxi_button_open_waiting_window(self, driver_and_order_taxi):
        search_taxi_page = OrderTaxiPage(driver_and_order_taxi)

        assert search_taxi_page.get_title_text() == "Поиск машины"

    @allure.title("Элементы окна ожидания машины соответствуют ТЗ")
    def test_search_taxi_panel_elements_visible_and_have_expected_texts(self, driver_and_order_taxi):
        page = OrderTaxiPage(driver_and_order_taxi)

        assert (page.get_title_text() == WaitTaxiText.TITLE and
                page.is_timer_visible() and
                page.get_cancel_button_text() == WaitTaxiText.CANCEL_BUTTON and
                page.get_details_button_text() == WaitTaxiText.DETAILS_BUTTON)

    @allure.title("После окончания таймера отображается окно совершенного заказа")
    def test_timer_end_open_order_window(self, driver_and_order_taxi):
        page = OrderTaxiPage(driver_and_order_taxi)
        page.wait_for_zero_timer()

        assert WaitTaxiText.FINISH_ORDER in page.get_title_text()

    @allure.title("Нажатие кнопки Отмена закрывает окно поиска такси")
    @pytest.mark.xfail(reason="Кнопка Отменить не работает, заведен баг")
    def test_cancel_button_closes_search_window(self, driver_and_order_taxi):
        page = OrderTaxiPage(driver_and_order_taxi)
        page.click_cancel_button()  # Нажимаем кнопку Отменить

        assert page.is_search_window_closed()   # Проверяем, что окно поиска такси закрылось

    @allure.title("В деталях поездки отображается корректная стоимость тарифа")
    def test_details_show_correct_tariff_cost(self, driver_and_order_taxi):
        page = OrderTaxiPage(driver_and_order_taxi)
        page.click_details_button()  # Нажимаем кнопку Детали
        page.wait_for_details_panel_to_open()  # Ждем открытия панели деталей
        actual_cost = page.get_trip_cost_text()  # Получаем стоимость из деталей поездки

        # Проверяем, что стоимость содержит число (рубли)
        assert any(char.isdigit() for char in actual_cost), f"Стоимость '{actual_cost}' не содержит цифр"

    @allure.title("Кнопка Детали открывает панель с деталями поездки")
    def test_details_button_opens_details_panel(self, driver_and_order_taxi):
        page = OrderTaxiPage(driver_and_order_taxi)
        page.click_details_button()  # Нажимаем кнопку Детали
        page.wait_for_details_panel_to_open()  # Ждем открытия панели деталей

        # Проверяем, что панель с деталями отобразилась
        assert page.is_details_panel_visible(), "Панель деталей поездки не открылась после нажатия кнопки 'Детали'"

    @allure.title("Проверяем наличие блока 'Еще про поездку' в деталях поездки")
    def test_details_show_additional_info(self, driver_and_order_taxi):
        page = OrderTaxiPage(driver_and_order_taxi)
        page.click_details_button()
        page.wait_for_details_panel_to_open()

        additional_info = page.get_additional_info_title_text()

        assert "Еще про поездку" in additional_info, "Блок 'Еще про поездку' не найден"

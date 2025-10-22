from pages.base import BasePage
from locators.order_taxi_locators import OrderTaxiLocators
import allure


class OrderTaxiPage(BasePage):
    @allure.step("Получаем заголовок окна поиска такси")
    def get_title_text(self):
        return self.get_text_by_locator(OrderTaxiLocators.TAXI_TITLE)

    @allure.step("Получаем текст кнопки Отменить")
    def get_cancel_button_text(self):
        return self.get_text_by_locator(OrderTaxiLocators.CANCEL_BUTTON_TEXT)

    @allure.step("Получаем текст кнопки Детали")
    def get_details_button_text(self):
        return self.get_text_by_locator(OrderTaxiLocators.DETAILS_BUTTON_TEXT)

    @allure.step("Проверяем, что отображается таймер")
    def is_timer_visible(self):
        try:
            self.find_element_with_visibility_wait(OrderTaxiLocators.TIMER)
            return True
        except TimeoutError:
            return False

    @allure.step("ждем, пока таймер закончит отсчет")
    def wait_for_zero_timer(self):
        # с запасом в 1 секунду, чтобы функция успела отработать
        self.wait_text_is_visible(OrderTaxiLocators.TIMER, "00:01")
        # ждем, пока пройдет еще 1 секунда
        self.wait_change_of_element(OrderTaxiLocators.TIMER, "00:01")

    @allure.step("Нажимаем кнопку Отменить")
    def click_cancel_button(self):
        self.click_on_element(OrderTaxiLocators.CANCEL_BUTTON)

    @allure.step("Проверяем, закрылось ли окно поиска такси")
    def is_search_window_closed(self):
        return not self.element_is_visible(OrderTaxiLocators.TAXI_TITLE, timeout=3)

    @allure.step("Нажимаем кнопку Детали")
    def click_details_button(self):
        self.click_on_element(OrderTaxiLocators.DETAILS_BUTTON)

    @allure.step("Ждем открытия панели деталей поездки")
    def wait_for_details_panel_to_open(self):
        self.find_element_with_visibility_wait(OrderTaxiLocators.DETAILS_PANEL)

    @allure.step("Получаем текст стоимости поездки")
    def get_trip_cost_text(self):
        return self.get_text_by_locator(OrderTaxiLocators.TRIP_COST)

    @allure.step("Проверяем отображается ли блок с деталями поездки")
    def is_details_panel_visible(self):
        return self.element_is_visible(OrderTaxiLocators.DETAILS_PANEL)

    @allure.step("Получаем заголовок дополнительной информации из деталей поездки")
    def get_additional_info_title_text(self):
        return self.get_text_by_locator(OrderTaxiLocators.ADDITIONAL_INFO_TITLE)


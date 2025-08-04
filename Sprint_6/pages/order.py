import allure
from pages.base import BasePage
from locators.main_locators import MainLocators
from locators.order_locators import OrderLocators


class OrderPage(BasePage):
    @allure.step('Нажимаем на верхнюю кнопку "Заказать"')
    def click_top_button(self):
        self.click_on_element(MainLocators.ORDER_BUTTON_TOP)

    @allure.step('Нажимаем на нижнюю кнопку "Заказать"')
    def click_bottom_button(self):
        self.scroll_to_element(MainLocators.ORDER_BUTTON_LOW)
        self.click_on_element(MainLocators.ORDER_BUTTON_LOW)

    def get_text_title(self):
        return self.find_element_and_wait(OrderLocators.TITLE_ORDER).text

    @allure.step('Вводим информацию о клиенте')
    def fill_user_data(self, user):
        self.fill_text_by_element(OrderLocators.NAME, user['first_name'])
        self.fill_text_by_element(OrderLocators.SURNAME, user['surname'])
        self.fill_text_by_element(OrderLocators.ADDRESS, user['address'])

        self.click_on_element(OrderLocators.METRO_STATION)
        self.find_element_and_wait(OrderLocators.STATION_SELECTION)
        self.click_on_element(OrderLocators.STATION_SELECTION)

        self.fill_text_by_element(OrderLocators.PHONE, user['phone_number'])
        self.click_on_element(OrderLocators.BUTTON_NEXT)

    @allure.step('Заполняем форму о времени и сроке доставки')
    def fill_order_details(self, user):
        self.fill_text_by_element(OrderLocators.DATE_SELECTED, user['delivery_date'])
        self.click_on_element(OrderLocators.RENTAL_PERIOD)
        self.click_on_element(OrderLocators.SELECT_DAY)

        if user['color'] == 'black':
            self.click_on_element(OrderLocators.COLOR_OF_SCOOTER_BLACK)
        elif user['color'] == 'gray':
            self.click_on_element(OrderLocators.COLOR_OF_SCOOTER_GREY)

        self.fill_text_by_element(OrderLocators.COMMENT_BY_COURIER, user['comment'])

    @allure.step('Оформляем заказ и подтверждаем его')
    def order_scooter(self):
        self.click_on_element(OrderLocators.LOWER_BUTTON)
        self.click_on_element(OrderLocators.BUTTON_YES)

    @allure.step('Проверяем заказ')
    def check_scooter_status(self):
        return self.find_element_and_wait(OrderLocators.ORDER_STATUS).text

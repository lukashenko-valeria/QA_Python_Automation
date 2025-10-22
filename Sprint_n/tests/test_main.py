from pages.main import MainPage
from  locators.main_page_locators import MainLocators
import allure
from data import ADDRESS_ONE, ADDRESS_TWO


@allure.suite("Тесты главной страницы")
class TestMainPage:
    @allure.title("Проверяем отрисовку точек начала и конца маршрута") # Задание 1.Отрисовка маршрута
    def test_points_of_route_on_the_map(self, driver): # тест готов
        main = MainPage(driver)
        main.input_start_address(ADDRESS_ONE)
        main.input_end_address(ADDRESS_TWO)
        points = main.get_list_of_travel_points()

        assert len(points) == 2

    @allure.title("Проверяем отображение блока с выбранным маршрутом при вводе разных адресов")
    def test_points_of_route_on_the_map_and_two_different_address(self, driver): # Задание 2. Отрисовка блока с выбором маршрута при вводе разных адресов
        main = MainPage(driver)
        main.input_start_address(ADDRESS_ONE)
        main.input_end_address(ADDRESS_TWO)

        assert main.visibility_of_route_panel()

    @allure.title("Проверяем отображение блока с выбранным маршрутом при вводе одинаковых адресов")
    def test_points_of_route_on_the_map_and_two_same_address(self, driver):  # Задание 2. Отрисовка блока с выбором маршрута Авто Бесплатно при вводе одинаковых адресов
        main = MainPage(driver)
        main.input_start_address(ADDRESS_TWO)
        main.input_end_address(ADDRESS_TWO)
        text = main.get_text_by_locator(MainLocators.FREE_CAR)
        duration = main.get_text_by_locator(MainLocators.FREE_DURATION)

        assert 'Авто Бесплатно' in text
        assert 'В пути 0 мин.' in duration

    @allure.title("Проверяем переключение между видами маршрутов (Оптимальный\Быстрый)")
    def test_switching_between_route_types(self, driver): # Задание 3.1. Подготовка к заказу такси. При переключении между видами маршрута (Оптимальный\Быстрый) происходит смена активного таба и пересчет времени и стоимости маршрута
        main = MainPage(driver)
        main.input_addresses()

        text_quick = main.get_fast_tab_text() # получаем текст вкладки Быстрый
        price = main.get_text_from_price_description() # получаем стоимость поездки

        main.click_route(MainLocators.OPTIM)

        price_new = main.get_text_from_price_description() # получаем стоимость поездки на другой вкладке
        text_optim = main.get_optimal_tab_text() # получаем текст вкладки Оптимальный

        assert text_optim != text_quick # сравниваем названия вкладок
        assert "Оптимальный" in text_optim and "Быстрый" in text_quick  # убеждаемся, что вкладки переключались
        assert price != price_new

    @allure.title("Проверяем переключение на тариф Свой и становятся активными типы передвижения")
    def test_switching_own_route_types(self, driver):  # Задание 3.2.  Подготовка к заказу такси. При переключении на вид маршрута Свой происходит смена активного таба и становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)
        main = MainPage(driver)
        main.input_addresses()
        text_quick = main.get_fast_tab_text()  # получаем текст вкладки Быстрый
        main.click_route(MainLocators.OWN)  # переключаемся на вкладку Свой
        text_own = main.get_own_tab_text()  # получаем текст вкладки Свой

        assert text_quick != text_own
        assert main.all_options_activity() # получаем активность всех опций

    @allure.title("Проверяем активность кнопки Вызвать такси при выборе тарифа Быстрый")
    def test_call_taxi_activity_route_quick(self, driver): # Задание 3.3. При выборе вида маршрута Быстрый активна кнопка Вызвать такси
        main = MainPage(driver)
        main.input_addresses()
        text = main.get_text_by_locator(MainLocators.BUTTON_CALL_TAXI)

        assert 'Вызвать такси' in text

    @allure.title("Проверяем активность кнопки Забронировать при выборе тарифа Свой и типа Драйв")
    def test_book_button_active_on_own_tariff_with_drive(self, driver):  # Задание 3.4. При выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать
        main = MainPage(driver)
        main.input_addresses()
        main.call_own_taxi_route()
        button_text = main.get_book_button_text()

        assert 'Забронировать' in button_text

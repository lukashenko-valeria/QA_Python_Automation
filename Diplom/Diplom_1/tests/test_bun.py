import allure
from bun import Bun
import pytest


@allure.suite("Тестируем класс Bun")
class TestBun():
    @allure.title('Присваиваем название булочке, используя разные значения длины при корректной цене')
    @pytest.mark.parametrize("name, price", [("Краторная булка", 1255.0), ("", 500.0), ("Длинное название Флюорисцентной и Краторной булки с дополнительной длиной", 999.99),("Булка", 100.0)])
    def test_get_name_returns_correct_name(self,name, price):
        bun = Bun(name, price)
        result_name = bun.get_name()
        assert type(result_name) == str and result_name == name

    @allure.title('Присваиваем цену булочке, используя различные варианты, при корректном названии')
    @pytest.mark.parametrize("name, price", [("Краторная булка", 1255.0), ("Краторная булка", -100.0), ("Бесплатная булка", 0.0)])
    def test_get_price_returns_correct_price(self, name, price):
        bun = Bun(name, price)
        result_price = bun.get_price()
        assert type(result_price) == float and result_price == price

    @allure.title("Проверка установки целочисленной цены - возвращает int - тот же тип, что указали в __init__")
    def test_init_integer_price_return_integer(self):
        bun = Bun("Простая булка", 500)
        bun_price = bun.get_price()
        assert type(bun_price) == int
        assert bun_price == 500.0

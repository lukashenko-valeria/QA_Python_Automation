import pytest
import allure
from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@allure.suite("Тестируем класс Database")
class TestDatabase:
    @allure.title("Проверяем возвращение списка функцией available_buns")
    def test_available_buns_return_list_bun(self):
        db = Database()
        result = db.available_buns()
        assert type(result) == list
        assert len(result) == 3

    @allure.title("Проверяем корректность полученных данных для названия булочки")
    @pytest.mark.parametrize("index, expected_name, expected_price", [(0, "black bun", 100), (1, "white bun", 200), (2, "red bun", 300)])
    def test_available_buns_get_correct_data_bun(self, index, expected_name, expected_price):
        self.db = Database()
        buns = self.db.available_buns()

        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price

    @allure.title("Проверяем получение списка данных для ингредиентов")
    def test_available_ingredients_get_correct_list_ingredient(self):
        self.db = Database()
        result = self.db.available_ingredients()
        assert type(result) == list
        assert len(result) == 6

    @allure.title("Проверяем корректность полученных данных для ингредиентов")
    @pytest.mark.parametrize("index, expected_type, expected_name, expected_price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300)
    ])
    def test_available_ingredients_get_correct_data_ingredient(self, index, expected_type, expected_name, expected_price):
        self.db = Database()
        ingredients = self.db.available_ingredients()

        assert ingredients[index].get_type() == expected_type  # проверяем  ингредиент по индексу
        assert ingredients[index].get_name() == expected_name
        assert ingredients[index].get_price() == expected_price

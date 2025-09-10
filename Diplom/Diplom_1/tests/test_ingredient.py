import allure
import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE
from ingredient_types import INGREDIENT_TYPE_FILLING


@allure.suite("Тестируем класс Ingredient")
class TestIngredient:
    @allure.title("Тестируем установку и получение цены для разных значений")
    @pytest.mark.parametrize('price', (0.0, 100.0, 100))
    def test_get_price_return_preset_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", price)
        assert ingredient.get_price() == price

    @allure.title("Тестируем установку и получение названия ингредиента для разных значений")
    @pytest.mark.parametrize('name', ("", "hot sauce"))
    def test_get_name_return_preset_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name, 100.0)
        assert ingredient.get_name() == name

    @allure.title("Тестируем получение типа ингредиента")
    @pytest.mark.parametrize("ingredient_type", (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING))
    def test_get_type_return_preset_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "hot sauce", 100.0)
        assert ingredient.get_type() == ingredient_type

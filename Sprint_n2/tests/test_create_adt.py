from methods.create_adt_methods import CreateAdtMethods
import pytest
import allure
from helpers.data import CATEGORIES

@allure.suite("Тестируем создание объявления")
class TestCreateAdvert:

    @allure.title("Создаем объявления всех возможных категорий (параметризация)")
    @pytest.mark.parametrize("category", CATEGORIES)
    def test_create_new_order_status_code_created(self, get_auth_token, category):
        status_code, json = CreateAdtMethods.create_new_order(get_auth_token, category)
        assert status_code == 201 and json["category"] == category

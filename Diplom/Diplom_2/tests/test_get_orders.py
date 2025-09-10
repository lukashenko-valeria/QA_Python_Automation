import allure
import requests
import random
from data import Urls
from helpers import generate_user_data

@allure.suite("Тестируем получение заказов")
class TestGetOrders:
    @allure.title('Получение заказов авторизованного пользователя')
    def test_success_request_user_orders(self):
        user = generate_user_data()
        created_user_response = requests.post(f'{Urls.burger_url}{Urls.register_user}', json=user)  # Создаём нового пользователя
        access_token = created_user_response.json()['accessToken']

        ingredients = requests.get(f'{Urls.burger_url}{Urls.ingredients}')
        ingredients_info = ingredients.json()
        ingredients_list = ingredients_info['data']  # создаем список всех ингредиентов
        selected_ingredients = random.sample(ingredients_list, random.randint(2, 4))
        ingredient_id = [ingredient['_id'] for ingredient in selected_ingredients]

        data = {
            "ingredients": ingredient_id
        }
        requests.post(f'{Urls.burger_url}{Urls.order}', json=data)

        orders_response = requests.get(
            f'{Urls.burger_url}{Urls.order}',  # предполагая Urls.orders = '/api/orders'
            headers={'Authorization': access_token}
        )
        orders_data = orders_response.json()

        assert created_user_response.status_code == 200 and created_user_response.json()['success']
        assert orders_response.status_code == 200 and orders_data['success']
        assert 'orders' in orders_data
        assert 'total' in orders_data
        assert 'totalToday' in orders_data

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_success_create_user_orders(self):
        ingredients = requests.get(f'{Urls.burger_url}{Urls.ingredients}')
        ingredients_info = ingredients.json()
        ingredients_list = ingredients_info['data']  # создаем список всех ингредиентов
        selected_ingredients = random.sample(ingredients_list, random.randint(2, 4))
        ingredient_id = [ingredient['_id'] for ingredient in selected_ingredients]

        data = {
            "ingredients": ingredient_id
        }
        order_response = requests.post(f'{Urls.burger_url}{Urls.order}', json=data)

        get_orders_response = requests.get(f'{Urls.burger_url}{Urls.order}')

        assert order_response.status_code == 200
        assert get_orders_response.status_code == 401

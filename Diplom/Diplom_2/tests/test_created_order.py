import allure
import requests
import random
from data import Urls, Messages
from helpers import generate_user_data


@allure.suite("Тестируем создание заказа")
class TestCreatedOrder:
    @allure.title('Создание заказа с ингредиентами авторизованным пользователем')
    def test_success_create_order_with_ingredients_authorized_user(self):
        user = generate_user_data()
        created_user_response = requests.post(f'{Urls.burger_url}{Urls.register_user}', json=user)  # Создаём нового пользователя
        access_token = created_user_response.json()['accessToken']  # получаем токен зарегистрированного пользователя

        ingredients = requests.get(f'{Urls.burger_url}{Urls.ingredients}')
        ingredients_info = ingredients.json()
        ingredients_list = ingredients_info['data']   # создаем список всех ингредиентов
        selected_ingredients = random.sample(ingredients_list, random.randint(2, 4))
        ingredient_id = [ingredient['_id'] for ingredient in selected_ingredients]

        data = {
            "ingredients": ingredient_id
        }
        order_response = requests.post(f'{Urls.burger_url}{Urls.order}', json=data, headers={'Authorization': access_token})
        order_info = order_response.json()

        assert created_user_response.status_code == 200 and order_response.status_code == 200 and order_info['success']
        assert 'name' in order_info and 'order' in order_info
        assert 'number' in order_info['order']

    @allure.title('Создание заказа с ингредиентами неавторизованным пользователем')
    def test_create_order_with_ingredients_unauthorized_user(self):
        ingredients = requests.get(f'{Urls.burger_url}{Urls.ingredients}')
        ingredients_info = ingredients.json()
        ingredients_list = ingredients_info['data']  # создаем список всех ингредиентов
        selected_ingredients = random.sample(ingredients_list, random.randint(2, 4))
        ingredient_id = [ingredient['_id'] for ingredient in selected_ingredients]

        data = {
            "ingredients": ingredient_id
        }
        order_response = requests.post(f'{Urls.burger_url}{Urls.order}', json=data)  # создаем заказ с ингредиентами неавторизованным пользователем
        order_info = order_response.json()

        # заказы неавторизованным пользователем создаются, это известный баг; уточнить его оформление
        assert order_response.status_code == 200 and order_info['success']
        assert 'name' in order_info and 'order' in order_info
        assert 'number' in order_info['order']

    @allure.title('Создание заказа без ингредиентов авторизованным пользователем')
    def test_create_order_without_ingredients_authorized_user(self):
        user = generate_user_data()
        created_user_response = requests.post(f'{Urls.burger_url}{Urls.register_user}', json=user)  # Создаём нового пользователя
        access_token = created_user_response.json()['accessToken']  # получаем токен зарегистрированного пользователя
        data = {
            "ingredients": []
        }
        order_response = requests.post(f'{Urls.burger_url}{Urls.order}', json=data, headers={'Authorization': access_token}) # создаем заказ без ингредиентов
        order_info = order_response.json()

        assert created_user_response.status_code == 200
        assert order_response.status_code == 400 and order_info['success'] == False

    @allure.title('Создание заказа без ингредиентов неавторизованным пользователем')
    def test_create_order_without_ingredients_unauthorized_user(self):
        data = {
            "ingredients": []
        }
        order_response = requests.post(f'{Urls.burger_url}{Urls.order}', json=data)  # создаем заказ без ингредиентов
        order_info = order_response.json()

        assert order_response.status_code == 400
        assert order_info['success'] == False

    @allure.title('Создание заказа с неверным хешем ингредиентов авторизованным пользователем')
    def test_invalid_create_order_with_wrong_ingredients(self):
        user = generate_user_data()
        created_user_response = requests.post(f'{Urls.burger_url}{Urls.register_user}', json=user)  # Создаём нового пользователя
        access_token = created_user_response.json()['accessToken']  # получаем токен зарегистрированного пользователя

        data = {
            "ingredients": ["55561c0c5a71d1f82001bdaaa6d"] # неверный хеш ингредиентов
        }
        order_response = requests.post(f'{Urls.burger_url}{Urls.order}', json=data, headers={'Authorization': access_token})

        assert created_user_response.status_code == 200
        assert Messages.INTERNAL_SERVER_ERROR in order_response.text

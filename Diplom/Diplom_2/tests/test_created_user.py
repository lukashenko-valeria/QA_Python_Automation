import allure
import requests
import pytest
from data import Urls, InvalidUser, Messages
from helpers import generate_user_data


@allure.suite("Тестируем создание заказа")
class TestCreatedUser:

    @allure.title('Успешное создание нового пользователя')
    def test_success_create_user(self):
        user = generate_user_data()
        created_user_response = requests.post(f'{Urls.burger_url}{Urls.register_user}', json=user)  # Создаём нового пользователя
        assert created_user_response.status_code == 200 and created_user_response.json()["success"]

    @allure.title('Попытка создания пользователя, который уже зарегистрирован')  #  работает, успешно создает нового пользователя
    def test_create_double_user(self):
        user = generate_user_data()
        user_response = requests.post(f'{Urls.burger_url}{Urls.register_user}', json=user)  # Создаём нового пользователя
        user_2_response = requests.post(f'{Urls.burger_url}{Urls.register_user}', json=user) # повторно создаём нового пользователя с такими же данными
        user_2_info = user_2_response.json()

        assert user_response.status_code == 200 and user_response.json()["success"]
        assert user_2_response.status_code == 403

        assert user_2_info['success'] == False
        assert user_2_info['message'] == Messages.USER_ALREADY_EXISTS

    @allure.title('Неуспешное создание пользователя, с одним из незаполненных полей')
    @pytest.mark.parametrize('invalid_data', [InvalidUser.data, InvalidUser.data_2])
    def test_success_create_double_user(self, invalid_data):
        failed_user_response = requests.post(f'{Urls.burger_url}{Urls.register_user}', json=invalid_data)  # Создаём нового пользователя без однлго из обязательных полей
        user_info = failed_user_response.json()
        assert failed_user_response.status_code == 403
        assert user_info['message'] == Messages.REQUIRED_FIELDS
        assert user_info['success'] == False

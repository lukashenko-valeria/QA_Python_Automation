import allure
import requests
from data import Urls, Messages
from helpers import generate_user_data

@allure.suite("Тестируем логин пользователя")
class TestLogin:
    @allure.title('Авторизация под существующим пользователем')
    def test_authorization_real_user(self):
        user = generate_user_data()
        created_user_response = requests.post(f'{Urls.burger_url}{Urls.register_user}', json=user)  # Создаём нового пользователя
        assert created_user_response.status_code == 200 and created_user_response.json()["success"]
        user_credentials = {
            'email': user['email'],
            'password': user['password']
        }
        authorized_user_response = requests.post(f'{Urls.burger_url}{Urls.login}', json=user_credentials)  # авторизуемся с такими же учетными данными
        auth_user_info = authorized_user_response.json()
        assert authorized_user_response.status_code == 200 and auth_user_info["success"]
        assert auth_user_info['user']['email'] == user_credentials['email']

    @allure.title('Авторизация с неверным логином и паролем')
    def test_invalid_login(self):
        wrong_user_data = {
            'email': 'wrong_email',
            'password': 'wrong_password'
        }
        authorized_user_response = requests.post(f'{Urls.burger_url}{Urls.login}', json=wrong_user_data)  # авторизуемся с несуществующими же данными
        assert authorized_user_response.status_code == 401
        assert authorized_user_response.json()['message'] == Messages.INCORRECT_CREDENTIALS

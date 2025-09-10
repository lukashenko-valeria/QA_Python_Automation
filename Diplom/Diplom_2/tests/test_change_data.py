import allure
import requests
from fakers import generated_email, generated_login
from data import Urls, Messages
from helpers import generate_user_data

@allure.suite("Тестируем изменение данных пользователя")
class TestChange:

    @allure.title('Изменяем данные пользователя авторизованным пользователем - email')
    def test_change_user_data_email(self):
        user = generate_user_data()
        created_user_response = requests.post(f'{Urls.burger_url}{Urls.register_user}', json=user)  # Создаём нового пользователя
        user_info = created_user_response.json()
        assert created_user_response.status_code == 200 and user_info['success']

        access_token = user_info['accessToken']  # получаем токен зарегистрированного пользователя
        new_email = generated_email()   # генерируем изменяемый email
        new_data = {
            'email': new_email,
            'name': user['name']
        }

        user_change_response = requests.patch(f'{Urls.burger_url}{Urls.user_info}', json=new_data, headers={'Authorization': access_token}) # меняем данные пользователя
        user_change_info = user_change_response.json()  # получаем информацию о созданном пользователе
        assert user_change_response.status_code == 200 and user_change_info['success']
        assert user_change_info['user']['email'] == new_email # измененный email!
        assert user_change_info['user']['name'] == user['name']

    @allure.title('Изменяем данные пользователя авторизованным пользователем - name')
    def test_change_user_data_name(self):
        user = generate_user_data()
        created_user_response = requests.post(f'{Urls.burger_url}{Urls.register_user}', json=user)  # Создаём нового пользователя
        user_info = created_user_response.json()
        assert created_user_response.status_code == 200

        access_token = user_info['accessToken']  # получаем токен зарегистрированного пользователя
        new_name = generated_login()
        new_data = {
            'email': user['email'],
            'name': new_name
        }
        user_change_response = requests.patch(f'{Urls.burger_url}{Urls.user_info}', json=new_data, headers={'Authorization': access_token})  # меняем данные пользователя
        user_change_info = user_change_response.json()  # получаем информацию о созданном пользователе
        assert user_change_response.status_code == 200 and user_change_info['success']
        assert user_change_info['user']['email'] == user['email']
        assert user_change_info['user']['name'] == new_name   # измененное имя пользователя

    @allure.title('Изменяем данные пользователя неавторизованным пользователем - email')
    def test_change_not_auth_user_data_email(self):
        user = generate_user_data()
        created_user_response = requests.post(f'{Urls.burger_url}{Urls.register_user}',
                                              json=user)  # Создаём нового пользователя

        new_email = generated_email()  # генерируем изменяемый email
        new_data = {
            'email': new_email,
            'name': user['name']
        }

        user_change_response = requests.patch(f'{Urls.burger_url}{Urls.user_info}', json=new_data)  # меняем данные пользователя
        user_info = user_change_response.json()  # получаем информацию об ошибке

        assert created_user_response.status_code == 200 and created_user_response.json()['success']
        assert user_change_response.status_code == 401
        assert user_info['message'] == Messages.SHOULD_BE_AUTHORIZED and user_info['success'] == False

    @allure.title('Изменяем данные пользователя неавторизованным пользователем - name')
    def test_change_not_auth_user_data_name(self):
        user = generate_user_data()
        created_user_response = requests.post(f'{Urls.burger_url}{Urls.register_user}', json=user)  # Создаём нового пользователя
        new_name = generated_login()
        new_data = {
            'email': user['email'],
            'name': new_name
        }
        user_data_change = requests.patch(f'{Urls.burger_url}{Urls.user_info}', json=new_data)  # меняем данные пользователя
        user_info = user_data_change.json()  # получаем информацию об ошибке

        assert created_user_response.status_code == 200 and created_user_response.json()['success']
        assert user_data_change.status_code == 401
        assert user_info['message'] == Messages.SHOULD_BE_AUTHORIZED and user_info['success'] == False

    @allure.title('Удаляем пользователя')
    def test_delete_user(self):
        user = generate_user_data()
        created_user_response = requests.post(f'{Urls.burger_url}{Urls.register_user}', json=user)  # Создаём нового пользователя
        user_info = created_user_response.json()

        access_token = user_info['accessToken']  # получаем токен зарегистрированного пользователя

        user_delete_response = requests.delete(f'{Urls.burger_url}{Urls.user_info}', headers={'Authorization': access_token})  # удаляем пользователя
        assert created_user_response.status_code == 200 and user_info['success']
        assert user_delete_response.status_code == 202

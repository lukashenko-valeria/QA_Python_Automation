import requests
from helpers.data import Urls
import allure
from helpers.fakers import generate_user_data


class Users:

    @staticmethod
    @allure.step("Создание нового пользователя")
    def create_user():
        user = generate_user_data()
        created_user_response = requests.post(f'{Urls.desk_url}{Urls.register_user}', json=user)
        return created_user_response, user  # Возвращаем и ответ, и данные пользователя

    @staticmethod
    @allure.step("Создание пользователя с уже зарегистрированным email")
    def create_user_duplicate_email():
        # Используем create_user для создания первого пользователя
        _, user_data = Users.create_user()
        # Повторно создаём пользователя с такими же данными
        second_response = requests.post(f'{Urls.desk_url}{Urls.register_user}', json=user_data)
        return second_response

    @staticmethod
    @allure.step("Авторизация пользователя")
    def _auth_user(user_data):
        user_credentials = {
            'email': user_data['email'],
            'password': user_data['password']
        }
        authorized_user_response = requests.post(f'{Urls.desk_url}{Urls.login}', json=user_credentials)
        return authorized_user_response

    @staticmethod
    @allure.step("Входим на сайт уже авторизованным пользователем")
    def create_and_auth_user():
        # Используем create_user для создания пользователя
        created_user_response, user_data = Users.create_user()
        # Используем приватный _auth_user для авторизации
        authorized_user_response = Users._auth_user(user_data)

        return {
            'user': user_data,
            'creation_response': created_user_response,
            'login_response': authorized_user_response
        }

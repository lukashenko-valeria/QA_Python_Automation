import allure
from methods.user_methods import Users


@allure.suite("Тестируем авторизацию уже созданного пользователя")
class TestLogin:

    @allure.title("Авторизация под существующим пользователем")
    def test_authorization_existing_user(self):
        authorized_response = Users.create_and_auth_user()
        creation_response = authorized_response['creation_response']
        login_response = authorized_response['login_response']
        user_data = authorized_response['user']
        auth_user_info = login_response.json()

        assert creation_response.status_code == 201
        assert auth_user_info['user']['email'] == user_data['email']
        assert login_response.status_code == 201

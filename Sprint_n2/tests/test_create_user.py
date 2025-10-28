import allure
from methods.user_methods import Users


@allure.suite("Тестируем создание нового пользователя")
class TestCreateUser:

    @allure.title("Успешное создание нового пользователя")
    def test_success_user_creation(self):
        created_user_response, _ = Users.create_user()

        assert created_user_response.status_code == 201, f"Ожидалось 201, получено {created_user_response.status_code}"

        response_json = created_user_response.json()
        assert "user" in response_json
        assert "access_token" in response_json
        assert response_json["user"]["email"] is not None

    @allure.title("Попытка создания пользователя, который уже зарегистрирован")
    def test_create_double_user(self):
        created_user_2 = Users().create_user_duplicate_email()
        user_2_info = created_user_2.json()

        assert created_user_2.status_code == 400
        assert user_2_info['message'] == 'Почта уже используется'

import allure
from methods.update_adt_methods import UpdateAdtMethods
from helpers.fakers import generated_email
from methods.user_methods import Users
from methods.create_adt_methods import CreateAdtMethods


@allure.suite("Тестируем редактирование объявления")
class TestUpdateAdvert:

    @allure.title("Успешное редактирование объявления, созданного тем же пользователем")
    def test_update_advert_created_by_auth_user_status_code_200(self, get_auth_token_and_order_id):
        auth_token, order_id = get_auth_token_and_order_id
        new_name = generated_email()  # Генерируем случайный email для нового названия

        status_code, response_data = UpdateAdtMethods.change_order(auth_token, order_id, new_name)

        assert status_code == 200, f"Ожидался статус 200, получен {status_code}. Ответ: {response_data}"
        assert response_data["name"] == new_name, "Название объявления не обновилось"

    @allure.title("Редактирование объявления, созданного другим пользователем")
    def test_update_advert_not_created_by_auth_user_status_code_401(self, get_auth_token):
        # get_auth_token - токен другого пользователя, которым попытаемся чинить объявление,
        # созданное в этом тесте под пользователем user

        # Создаем второго пользователя и его объявление
        new_user_data = Users().create_and_auth_user()
        new_user_token = f"Bearer {new_user_data['login_response'].json()['token']['access_token']}"

        # Создаем объявление от имени второго пользователя
        status_code, created_advert = CreateAdtMethods.create_new_order(new_user_token, "Авто")
        assert status_code == 201, "Не удалось создать объявление для теста"
        other_user_order_id = created_advert["id"]

        # Пытаемся редактировать объявление второго пользователя под токеном первого пользователя
        new_name = generated_email()
        status_code, response_data = UpdateAdtMethods.change_order(
            get_auth_token,  # Токен первого пользователя
            other_user_order_id,  # ID объявления второго пользователя
            new_name
        )

        assert status_code == 401, f"Ожидался статус 401, получен {status_code}. Ответ: {response_data}"

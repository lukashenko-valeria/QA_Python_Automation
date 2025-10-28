import allure
from methods.delete_adt_methods import DeleteAdtMethods
from helpers.data import SUCCESSFUL_DELETE_TEXT

@allure.suite("Тестируем удаление объявления")
class TestDeleteAdvert:

    @allure.title("Успешное удаление объявления, созданного тем же пользователем")
    def test_delete_order_created_by_auth_user_status_code_200(self, get_auth_token_and_order_id):
        auth_token, order_id = get_auth_token_and_order_id

        status_code, response_data = DeleteAdtMethods.delete_order(auth_token, order_id)

        assert status_code == 200, f"Ожидался статус 200, получен {status_code}. Ответ: {response_data}"
        assert response_data["message"] == SUCCESSFUL_DELETE_TEXT, "Сообщение об удалении не соответствует ожидаемому"

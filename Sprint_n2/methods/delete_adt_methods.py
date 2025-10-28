import requests
from helpers.data import Urls
import allure


class DeleteAdtMethods:

    @staticmethod
    @allure.step("Удаляем объявление с помощью HTTP-метода DELETE")
    def delete_order(auth_token, order_id):
        """
        Статический метод для удаления существующего объявления

        Args:
            auth_token (str): Токен авторизации
            order_id (str): ID объявления для удаления

        Returns:
            tuple: (status_code, response_data)
        """
        url = f"{Urls.desk_url}{Urls.delete_adt}{order_id}"

        headers = {
            "Authorization": auth_token
        }

        response = requests.delete(url=url, headers=headers)
        return response.status_code, response.json()

import requests
from requests_toolbelt import MultipartEncoder
from helpers.data import Urls
import allure


class UpdateAdtMethods:

    @staticmethod
    @allure.step("Редактируем объявление с помощью HTTP-метода PATCH")
    def change_order(auth_token, order_id, new_name):
        """
        Статический метод для редактирования существующего объявления

        Args:
            auth_token (str): Токен авторизации
            order_id (str): ID объявления для редактирования
            new_name (str): Новое название объявления

        Returns:
            tuple: (status_code, response_data)
        """
        url = f"{Urls.desk_url}{Urls.update_adt}{order_id}"

        payload = MultipartEncoder(fields={
            "name": new_name,
            "category": "Авто",
            "condition": "Новый",
            "city": "Москва",
            "description": "",
            "price": "1000",
            "img1": None,
            "img2": None,
            "img3": None
        })

        headers = {
            "Authorization": auth_token,
            "Content-Type": payload.content_type
        }

        response = requests.patch(url=url, headers=headers, data=payload)
        return response.status_code, response.json()

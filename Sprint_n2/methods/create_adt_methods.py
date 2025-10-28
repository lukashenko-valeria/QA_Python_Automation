import requests
from requests_toolbelt import MultipartEncoder
from helpers.data import Urls
import allure


class CreateAdtMethods:

    @staticmethod
    @allure.step("Создаем объявление с указанной категорией HTTP-методом POST")
    def create_new_order(auth_token, order_category):
        """
        Статический метод для создания нового объявления

        Args:
            auth_token (str): Токен авторизации
            order_category (str): Категория объявления

        Returns:
            tuple: (status_code, response_data)
        """

        payload = MultipartEncoder(fields={
            "name": "advert_name",
            "category": order_category,
            "condition": "Новый",
            "city": "Москва",
            "description": "",
            "price": "100"
        })

        headers = {
            "Authorization": auth_token,
            "Content-Type": payload.content_type
        }

        response = requests.post(url=Urls.desk_url + Urls.create_adt, headers=headers, data=payload)
        return response.status_code, response.json()

    @staticmethod
    @allure.step("Создаем объявление и возвращаем его id")
    def get_new_order_id(auth_token, order_category):
        """
        Статический метод для создания объявления и получения его ID

        Args:
            auth_token (str): Токен авторизации
            order_category (str): Категория объявления

        Returns:
            str or None: ID созданного объявления или None при ошибке
        """
        status_code, response_data = CreateAdtMethods.create_new_order(auth_token, order_category)

        if status_code == 201 and isinstance(response_data, dict):
            return response_data.get("id")
        return None

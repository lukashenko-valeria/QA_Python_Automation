import pytest
import allure
import requests
from methods.create_adt_methods import CreateAdtMethods
from helpers.data import Urls
from helpers.data import AUTH_DATA

@allure.title("Авторизируемся и возвращаем токен")
@pytest.fixture
def get_auth_token():
    url = Urls.desk_url + Urls.login
    response = requests.post(url=url, data=AUTH_DATA)
    return "Bearer " + response.json()["token"]["access_token"]

@allure.title("Авторизируемся, создаем объявление, возвращаем токен и id объявления")
@pytest.fixture
def get_auth_token_and_order_id(get_auth_token):
    order_id = CreateAdtMethods.get_new_order_id(get_auth_token, "Авто")
    return get_auth_token, order_id

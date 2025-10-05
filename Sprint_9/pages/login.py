import time
import allure
from pages.base import BasePage
from locators.login_locators import LoginPageLocators
from data.data import Urls
from data.fakers import generated_email, generated_password, generated_last_name, generated_first_name, generated_login


class LoginPage(BasePage):
    @allure.step("Открываем страницу входа или создания аккаунта")
    def open(self):
        self.open_page(Urls.REGISTRATION_URL)

    @allure.step('Вводим данные пользователя')
    def create_email_and_password(self):
        email = generated_email()
        password = generated_password()

        self.input_text(LoginPageLocators.EMAIL_FIELD, email)
        self.input_text(LoginPageLocators.PASSWORD_FIELD, password)
        return email, password

    @allure.step('Нажимаем кнопку "Создать аккаунт"')
    def click_on_button_create_account(self, locator):
        self.click_on_element(locator)

    @allure.title('Вводим данные нового пользователя')
    def input_user_data_return_name(self, email, password):
        user_name = generated_login()
        self.input_text(LoginPageLocators.NAME, generated_first_name())
        self.input_text(LoginPageLocators.LAST_NAME, generated_last_name())
        self.input_text(LoginPageLocators.LOGIN, user_name)
        self.input_text(LoginPageLocators.EMAIL, email)
        self.input_text(LoginPageLocators.PASSWORD, password)
        return user_name

    @allure.title('Создаем нового пользователя')
    def create_new_account(self):
        email, password = self.create_email_and_password()
        self.click_on_button_create_account(LoginPageLocators.ENTER_BUTTON_CREATE)
        self.input_user_data_return_name(email, password)
        self.click_on_button_create_account(LoginPageLocators.ENTER_BUTTON_CREATE_LOW)

        # Ожидаем редирект на страницу входа
        self.wait_for_url('signin')
        return email, password

    @allure.title('Входим в аккаунт и переходим на страницу создания рецептов')
    def authorize_and_open_recipe_page(self):
        email, password = self.create_email_and_password()
        self.click_on_button_create_account(LoginPageLocators.ENTER_BUTTON_CREATE)
        user_name = self.input_user_data_return_name(email, password)
        self.click_on_button_create_account(LoginPageLocators.ENTER_BUTTON_CREATE_LOW)

        # Ожидаем редирект на страницу входа после регистрации
        self.wait_for_url('signin')

        # Вводим данные для входа
        self.input_text(LoginPageLocators.EMAIL_FIELD, user_name)
        self.input_text(LoginPageLocators.PASSWORD_FIELD, password)

        # Нажимаем кнопку входа
        self.click_on_element(LoginPageLocators.ENTER_BUTTON_SIGNIN)

        # Ожидаем редирект на страницу рецептов
        self.wait_for_url('recipes')
        # Ожидаем появление кнопки выхода
        self.wait_for_text_in_element(LoginPageLocators.BUTTON_EXIT, 'Выход')

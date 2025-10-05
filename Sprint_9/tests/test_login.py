import allure
from locators.login_locators import LoginPageLocators
from pages.login import LoginPage

@allure.suite("Личный аккаунт")
class TestAccount:

    @allure.title("Создаем аккаунт")
    def test_create_new_account(self, driver):
        reg_page = LoginPage(driver)
        reg_page.open()
        reg_page.create_new_account()

        title = reg_page.get_text(LoginPageLocators.TITLE)

        assert reg_page.get_page_url().endswith('signin')
        assert 'Войти на сайт' in title

    @allure.title('Авторизуемся на сайте')
    def test_authorize_in_the_site(self, driver):
        auth_page = LoginPage(driver)
        auth_page.open()
        auth_page.authorize_and_open_recipe_page()

        exit_button = auth_page.get_text(LoginPageLocators.BUTTON_EXIT)

        assert auth_page.get_page_url().endswith('recipes')
        assert 'Выход' in exit_button

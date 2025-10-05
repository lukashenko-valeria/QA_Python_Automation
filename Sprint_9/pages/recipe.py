import allure
from pages.base import BasePage
from locators.login_locators import LoginPageLocators
from locators.recipe_locators import RecipePageLocators
from locators.recipe_card_locators import CardPageLocators
from data.data import Urls, RECIPE_USER, RECIPE_PASS
from pathlib import Path


class RecipePage(BasePage):
    @allure.step("Открываем страницу рецептов")
    def open(self):
        self.open_page(Urls.RECIPE_URL)

    @allure.title("Авторизуемся и открываем страницу создания рецепта")
    def authorize_and_open_page_creating_recipe(self):
        self.click_on_element(RecipePageLocators.SIGNIN)

        # Ожидаем загрузку формы авторизации
        self.wait_for_element(LoginPageLocators.EMAIL_FIELD)

        self.input_text(LoginPageLocators.EMAIL_FIELD, RECIPE_USER)
        self.input_text(LoginPageLocators.PASSWORD_FIELD, RECIPE_PASS)
        self.click_on_element(LoginPageLocators.ENTER_BUTTON_SIGNIN)

        # Ожидаем редирект после авторизации
        self.wait_for_url('recipes')
        self.open_page_creating_recipe()

    @allure.title("Открываем страницу создания рецептов")
    def open_page_creating_recipe(self):
        self.click_on_element(RecipePageLocators.CREATING_RECIPE)
        # Ожидаем загрузку формы создания рецепта
        self.wait_for_element(RecipePageLocators.NAME_RECIPE)

    @allure.title("Название рецепта")
    def name_recipe(self):
        self.input_text(RecipePageLocators.NAME_RECIPE, 'Жареная утка')

    @allure.title("Выбираем ингредиент")
    def ingredient_recipe(self):
        # Вводим текст и ждем появления списка
        self.input_text(RecipePageLocators.INGREDIENTS, 'утка')

        # Ожидаем появление списка ингредиентов
        self.wait_for_options_to_appear(RecipePageLocators.INGREDIENT_LIST)

        # Кликаем на первый элемент списка
        self.click_on_element(RecipePageLocators.INGREDIENT_LIST)

    @allure.title("Выбираем количество ингредиента")
    def ingredient_recipe_count(self):
        self.input_text(RecipePageLocators.INGREDIENT_WEIGHT, '200')

    @allure.title("Нажимаем 'Добавить ингредиент'")
    def add_ingredient(self):
        self.click_on_element(RecipePageLocators.INGREDIENT_ADD)
        # Ожидаем обновление списка ингредиентов
        self.wait_for_element(RecipePageLocators.ADDED_INGREDIENT)

    @allure.title("Указываем время приготовления")
    def add_time(self):
        self.input_text(RecipePageLocators.TIME_RECIPE, '60')

    @allure.title("Добавляем описание рецепта")
    def add_recipe_description(self):
        self.input_text(RecipePageLocators.DESCRIPTION, 'Тушеная утка')

    @allure.step("Загружаем картинку")
    def add_picture(self, picture_path):
        # Для скрытых input элементов используем find_hidden
        self.load_picture(RecipePageLocators.PICTURE_RECIPE, picture_path)

    @allure.step("Нажимаем кнопку создания рецепта")
    def create_recipe_button(self):
        # Скроллим к кнопке
        self.scroll_to_element(RecipePageLocators.CREATE_RECIPE)

        # Ожидаем и кликаем кнопку
        self.click_on_element(RecipePageLocators.CREATE_RECIPE, timeout=45)

        # Ожидаем редирект на страницу созданного рецепта
        self.wait_for_url('recipe')

    @allure.title("Создаем и загружаем рецепт")
    def create_and_upload_recipe(self, driver):
        self.authorize_and_open_page_creating_recipe()
        self.name_recipe()
        self.ingredient_recipe()
        self.ingredient_recipe_count()
        self.add_ingredient()
        self.add_time()
        self.add_recipe_description()

        # Вместо scroll_to_element для скрытого input используем обычный скролл вниз
        # и ожидаем доступность элемента в DOM
        self.scroll_down_page()
        self.wait_for_element(RecipePageLocators.PICTURE_RECIPE)  # Ждем presence, не visibility

        APP_DIR = Path(__file__).parent
        image_path = APP_DIR / '..' / 'assets' / 'duck.jpg'
        image_path_str = str(image_path.resolve())

        self.add_picture(image_path_str)
        self.create_recipe_button()

    @allure.step("Проверяем видимость кнопки добавления в список покупок")
    def is_add_to_shopping_list_button_visible(self):
        try:
            return self.find_element_with_visibility_wait(CardPageLocators.BUTTON_ADD, timeout=10)
        except Exception as e:
            print("Ошибка определения видимости кнопки добавления: ", e)
            return False

    @allure.step("Ожидаем загрузку страницы рецепта")
    def wait_for_recipe_page_load(self):
        self.wait_for_element(CardPageLocators.RECIPE_NAME_H1)
        self.wait_for_element(CardPageLocators.BUTTON_ADD)

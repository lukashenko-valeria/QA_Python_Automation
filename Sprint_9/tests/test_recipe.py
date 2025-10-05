import allure
from pages.recipe import RecipePage
from locators.recipe_card_locators import CardPageLocators


@allure.suite("Создание рецептов")
class TestRecipe:

    @allure.title("Создаем и загружаем рецепт")
    def test_create_and_upload_recipe(self, driver):
        recipe = RecipePage(driver)
        recipe.open()

        try:
            recipe.create_and_upload_recipe(driver)

            # Ожидаем полную загрузку страницы рецепта
            recipe.wait_for_recipe_page_load()

            # Проверяем результат
            current_url = recipe.get_page_url()
            print(f"Текущий URL: {current_url}")

            # Проверяем название рецепта
            name = recipe.get_text(CardPageLocators.RECIPE_NAME_H1)
            print(f"Название рецепта: {name}")

            # Проверяем кнопку
            is_button_visible = recipe.is_add_to_shopping_list_button_visible()
            print(f"Кнопка видима: {is_button_visible}")

            assert 'Жареная утка' in name, f"Ожидается 'Жареная утка', а получили: {name}"
            assert is_button_visible, "Кнопка добавления в корзину невидима"
            assert 'recipe' in current_url, f"URL должен содержать 'recipe', текущий URL: {current_url}"

        except Exception as e:
            # Делаем скриншот при ошибке
            driver.save_screenshot("/app/reports/error_screenshot.png")
            print(f"Ошибка теста: {e}")
            raise

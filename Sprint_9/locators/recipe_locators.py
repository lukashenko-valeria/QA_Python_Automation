from selenium.webdriver.common.by import By


class RecipePageLocators:
    SIGNIN = (By.XPATH, ".//*[@href='/signin']")
    CREATING_RECIPE = (By.XPATH, '//a[@href="/recipes/create" and text()="Создать рецепт"]')
    NAME_RECIPE = (By.CSS_SELECTOR, '.styles_inputField__3eqTj')

    INGREDIENTS = (By.XPATH, ".//div[text()='Ингредиенты']/../input")
    INGREDIENT_LIST = (By.XPATH, ".//div[contains(@class, 'ingredientsInput')]/div[contains(@class, 'styles_container')]")
    INGREDIENT_WEIGHT = (By.XPATH, ".//input[contains(@class, 'ingredientsAmountValue')]")
    INGREDIENT_ADD = (By.XPATH, ".//div[text()='Добавить ингредиент']")
    TIME_RECIPE = (By.XPATH, ".//div[text()='Время приготовления']/../input")
    DESCRIPTION= (By.XPATH, ".//div[text()='Описание рецепта']/../textarea")
    TAG = (By.XPATH, "//svg['http://www.w3.org/2000/svg']")
    PICTURE_RECIPE = (By.XPATH, ".//input[@type='file']")
    CREATE_RECIPE = (By.XPATH, ".//button[text()='Создать рецепт']")

    ADD_TO_SHOPPING_LIST_BUTTON_LOCATOR = (By.XPATH, ".//*[text()=' Добавить в покупки']")
    RECIPE_NAME_LOCATOR = (By.TAG_NAME, 'h1')

    ADDED_INGREDIENT = (By.XPATH, "//span[contains(@class, 'ingredient')]")  # пример
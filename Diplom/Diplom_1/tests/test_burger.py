import allure
from unittest.mock import Mock
from ..bun import Bun
from ..ingredient import Ingredient
from ..burger import Burger


@allure.suite("Тестируем класс Burger")
class TestBurger:

    # Тесты конструктора
    @allure.title("Тест инициализации бургера")
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    # Тесты метода set_buns
    @allure.title("Тест для булок - создаем моковую булочку для бургера")
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun
        assert burger.bun.get_price() == 100.0

    @allure.title("Проверяем добавление ингредиента в бургер")
    def test_add_ingredient_in_bun(self):
        burger = Burger()
        mock_ingredient = Mock()  # создаем моковый ингредиент
        mock_ingredient.configure_mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)  # добавляем моковый ингредиент
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    @allure.title("Проверяем перемещение ингредиента")
    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)  # создаем моковые ингредиенты
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient3 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient1)  # добавляем моковые ингредиенты
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
        burger.move_ingredient(2, 0)  # Перемещаем mock_ingredient3 с позиции 2 на позицию 0
        assert burger.ingredients[0] == mock_ingredient3
        assert burger.ingredients[1] == mock_ingredient1
        assert burger.ingredients[2] == mock_ingredient2

    @allure.title("Проверяем удаление ингредиента из бургера")
    def test_remove_ingredient_out_of_burger(self):
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)  # создаем моковые ингредиенты
        mock_ingredient2 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient1)  # добавляем моковые ингредиенты
        burger.add_ingredient(mock_ingredient2)
        burger.remove_ingredient(0)  # удаляем ингредиент из ingredients: [mock_ingredient1, mock_ingredient2] с индексом 0
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient2

    @allure.title("Получаем рецепт бургера")
    def test_get_receipt_with_ingredients(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Краторная булка"
        mock_bun.get_price.return_value = 100
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "Cheese"
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_price.return_value = 50

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert isinstance(receipt, str)
        assert "Краторная булка" in receipt
        assert "Cheese" in receipt

    @allure.title("Получаем цену двух булок и ингредиентов")
    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Краторная булка"
        mock_bun.get_price.return_value = 200
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "Cheese"
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_price.return_value = 100

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        actual_price = burger.get_price()
        expected_price = mock_bun.get_price() * 2 + mock_ingredient.get_price()

        assert actual_price == expected_price

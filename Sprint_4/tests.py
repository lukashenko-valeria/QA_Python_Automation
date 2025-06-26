from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_init_books_collector_right_attribute_lengths(self):
        books_collector = BooksCollector()
        assert (len(books_collector.get_books_genre()) == 0 and len(books_collector.favorites) == 0
                and len(books_collector.genre) == 5 and len(books_collector.genre_age_rating) == 2)

    def test_set_book_genre_add_new_book_twice_get_one_book_empty_genre(self):
        books_collector = BooksCollector()
        book = 'Война и мир'
        books_collector.add_new_book(book)
        books_collector.add_new_book(book)
        assert len(books_collector.get_books_genre()) == 1 and books_collector.get_book_genre(book) == ''

    @pytest.mark.parametrize('book_name', ['Оно', 'Пестрая лента', 'Винни-Пух'])
    def test_add_new_book_add_three_books_validate_name_positive(self, book_name):
        books_collector = BooksCollector()
        books_collector.add_new_book(book_name)
        assert book_name in books_collector.get_books_genre()

    @pytest.mark.parametrize('book_name', ['', 'Пестрая лента'*4])
    def test_add_new_book_add_two_books_validate_name_negative(self, book_name):
        books_collector = BooksCollector()
        books_collector.add_new_book(book_name)
        assert len(book_name) > 41 or len(book_name) == 0
        assert book_name not in books_collector.get_books_genre()

    @pytest.mark.parametrize('name, genre', [['Оно', 'Ужасы'], ['Винни-Пух', 'Мультфильмы']])
    def test_set_book_genre_add_new_book_set_genre(self, name, genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        film_genre = books_collector.get_book_genre(name)
        assert film_genre == genre

    @pytest.mark.parametrize('name, genre', [['Оно', 'Ужасы'], ['Пестрая лента', 'Детективы']])
    def test_get_books_with_specific_genre_filter_by_genre(self, name, genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        special_books = books_collector.get_books_with_specific_genre(genre)
        assert name in special_books

    @pytest.mark.parametrize('name, genre', [['Оно', 'Ужасы'], ['Пестрая лента', 'Детективы']])
    def test_get_books_genre_add_name_and_get_dictionary(self, name, genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_genre = books_collector.get_books_genre()
        assert name in books_genre
        assert books_genre[name] == genre

    @pytest.mark.parametrize('name, genre',
                             [['Винни Пух', 'Мультфильмы'], ['Один дома', 'Комедии'], ['Гостья из будущего', 'Фантастика']])
    def test_get_books_for_children_add_book_set_genre_and_get_books_for_children_positive(self, name, genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_for_children = books_collector.get_books_for_children()
        assert name in books_for_children

    @pytest.mark.parametrize('name, genre', [['Оно', 'Ужасы'], ['Пестрая лента', 'Детективы']])
    def test_get_books_for_children_add_book_set_genre_and_get_books_for_children_negative(self, name, genre):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_for_children = books_collector.get_books_for_children()
        assert name not in books_for_children

    @pytest.mark.parametrize('name', ['Оно', 'Пестрая лента', 'Винни-Пух'])
    def test_delete_book_from_favorites_add_book_and_delete_book(self, name):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)
        books_collector.delete_book_from_favorites(name)
        assert name not in books_collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name', ['Оно', 'Пестрая лента', 'Винни-Пух'])
    def test_get_list_of_favorites_books_add_book_and_get_favorites_list(self, name):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)
        favorites = books_collector.get_list_of_favorites_books()
        assert name in favorites

    @pytest.mark.parametrize('name', ['Оно', 'Пестрая лента', 'Винни-Пух'])
    def test_add_book_in_favorites_add_book_and_get_favorites(self, name):
        books_collector = BooksCollector()
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)
        assert name in books_collector.get_list_of_favorites_books()

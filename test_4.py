import pytest
from books_collector import BooksCollector

class TestBooksCollector:

    def test_add_new_book_adds_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_books_genre()

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert collector.get_books_genre() == {}

    def test_add_new_book_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('a' * 41)
        assert collector.get_books_genre() == {}

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_new_book('Книга')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Роман')
        assert collector.get_book_genre('Книга') == ''

    def test_set_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Нет', 'Фантастика')
        assert collector.get_book_genre('Нет') is None

    def test_get_book_genre_nonexistent(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Нет') is None

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Ужасы')
        collector.set_book_genre('Книга2', 'Комедии')
        result = collector.get_books_with_specific_genre('Ужасы')
        assert result == ['Книга1']

    def test_get_books_with_specific_genre_empty(self):
        collector = BooksCollector()
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == []

    def test_get_books_with_specific_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        result = collector.get_books_with_specific_genre('Роман')
        assert result == []

    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Мультфильмы')
        collector.set_book_genre('Книга2', 'Ужасы')
        result = collector.get_books_for_children()
        assert result == ['Книга1']

    def test_get_books_for_children_no_books(self):
        collector = BooksCollector()
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_books(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Нет')
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.delete_book_from_favorites('Книга')
        assert collector.get_list_of_favorites_books() == []
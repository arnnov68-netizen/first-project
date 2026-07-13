import pytest
class TestBooksCollector:

    def test_add_new_book_adds_book(self, books_collector):
        books_collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in books_collector.get_books_genre()

    @pytest.mark.parametrize("genre", ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_valid_genres(self, books_collector, genre):
        books_collector.add_new_book('Книга')
        books_collector.set_book_genre('Книга', genre)
        assert books_collector.get_book_genre('Книга') == genre

    def test_set_book_genre_overwrites_existing_genre(self, books_collector):
        books_collector.add_new_book('Книга')
        books_collector.set_book_genre('Книга', 'Фантастика')
        books_collector.set_book_genre('Книга', 'Ужасы')
        assert books_collector.get_book_genre('Книга') == 'Ужасы'

    def test_set_book_genre_valid(self, books_collector):
        books_collector.add_new_book('Книга')
        books_collector.set_book_genre('Книга', 'Фантастика')
        assert books_collector.get_book_genre('Книга') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self, books_collector):
        books_collector.add_new_book('Книга')
        books_collector.set_book_genre('Книга', 'Роман')
        assert books_collector.get_book_genre('Книга') == ''

    def test_set_book_genre_nonexistent_book(self, books_collector):
        books_collector.set_book_genre('Нет', 'Фантастика')
        assert books_collector.get_book_genre('Нет') is None

    def test_get_books_with_specific_genre(self, books_collector):
        books_collector.add_new_book('Книга1')
        books_collector.add_new_book('Книга2')
        books_collector.set_book_genre('Книга1', 'Ужасы')
        books_collector.set_book_genre('Книга2', 'Комедии')
        result = books_collector.get_books_with_specific_genre('Ужасы')
        assert result == ['Книга1']

    def test_get_books_with_specific_genre_empty(self, books_collector):
        result = books_collector.get_books_with_specific_genre('Фантастика')
        assert result == []

    def test_get_books_with_specific_genre_invalid_genre(self, books_collector):
        books_collector.add_new_book('Книга')
        result = books_collector.get_books_with_specific_genre('Роман')
        assert result == []

    def test_get_books_genre_returns_dict(self, books_collector):
        assert books_collector.get_books_genre() == {}

    def test_get_books_for_children(self, books_collector):
        books_collector.add_new_book('Книга1')
        books_collector.add_new_book('Книга2')
        books_collector.set_book_genre('Книга1', 'Мультфильмы')
        books_collector.set_book_genre('Книга2', 'Ужасы')
        result = books_collector.get_books_for_children()
        assert result == ['Книга1']

    def test_get_books_for_children_no_books(self, books_collector):
        assert books_collector.get_books_for_children() == []

    def test_add_book_in_favorites(self, books_collector):
        books_collector.add_new_book('Книга')
        books_collector.add_book_in_favorites('Книга')
        assert 'Книга' in books_collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_books(self, books_collector):
        books_collector.add_book_in_favorites('Нет')
        assert books_collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_duplicate(self, books_collector):
        books_collector.add_new_book('Книга')
        books_collector.add_book_in_favorites('Книга')
        books_collector.add_book_in_favorites('Книга')
        assert len(books_collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self, books_collector):
        books_collector.add_new_book('Книга')
        books_collector.add_book_in_favorites('Книга')
        books_collector.delete_book_from_favorites('Книга')
        assert books_collector.get_list_of_favorites_books() == []

import pytest
from books_collector import BooksCollector

@pytest.fixture
def books_collector():
    return BooksCollector()
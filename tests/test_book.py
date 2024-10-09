from models.book import Book
import pytest


@pytest.fixture
def book():
    return Book("Le petit prince", "Antoise Saint Exupéry", "123556789", "Je suis le roi des princes")


def test_book_creation(book):
    assert book.title == "Le petit prince"
    assert book.author == "Antoise Saint Exupéry"
    assert book.isbn == "123556789"
    assert book.summary == "Je suis le roi des princes"


def test_book_to_dict(book):
    book_dict = {"title": "Le petit prince",
               "author": "Antoise Saint Exupéry",
               "isbn": "123556789",
               "summary": "Je suis le roi des princes"}
    assert book.to_dict() == book_dict


def test_book_from_dict(book):
    book_dict = {"title": "Le petit prince",
               "author": "Antoise Saint Exupéry",
               "isbn": "123556789",
               "summary": "Je suis le roi des princes"}
    book_ = book.from_dict(book_dict)
    assert book_.title == "Le petit prince"
    assert book_.isbn == "123556789"


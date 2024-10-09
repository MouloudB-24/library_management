import pytest
from models.library import Library
from models.digital_Book import DigitalBook
from models.user import User


@pytest.fixture
def library():
    return Library("François Mitterand", "75000 Paris, France")


@pytest.fixture
def digital_book():
    return DigitalBook("Le petit prince", "Antoise Saint Exupéry", "123556789", "Je suis le roi des princes", "paper")


@pytest.fixture
def user():
    return User("Aylan", "0001A")


def test_library_creation(library):
    assert library.name == "François Mitterand"
    assert library.address == "75000 Paris, France"


def test_add_book_to_library(library, digital_book):
    library.add_digital_book(digital_book)
    assert len(library.available_books) == 1
    assert library.history_book[digital_book.to_dict()["title"]] == 0


def test_add_user_to_library(library, user):
    library.add_user(user)
    assert len(library.users) == 1
    assert library.history_user[user.to_dict()["name"]] == 0


def test_borrow_book(library, digital_book, user):
    library.borrow_book(digital_book.to_dict(), user.to_dict())
    assert len(library.available_books) == 0
    assert len(library.borrow_books) == 1
    assert library.history_book[digital_book.to_dict()["title"]] == 1


def test_return_book(library, digital_book, user):
    library.return_book(digital_book.to_dict())
    assert len(library.borrow_books) == 0
    assert len(library.available_books) == 1

from models.book import Book
from models.user import User


class Library:
    _instance = None

    def __new__(cls, name=None, address=None):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance.name = name
            cls._instance.address = address
            cls._instance.users = []
            cls._instance.available_books = []
            cls._instance.borrow_books = []
            cls._instance.history_book = {}
        return cls._instance

    def add_book(self, book):
        if isinstance(book, Book):
            self.available_books.append(book)
            self.history_book[book.title] = 0

    def delete_book(self, book):
        if isinstance(book, Book):
            self.available_books.remove(book)

    def borrow_book(self, book):
        self.borrow_books.append(self.available_books.pop(self.available_books.index(book)))
        self.history_book[book.title] += 1

    def return_book(self, book):
        self.available_books.append(self.borrow_books.pop(self.borrow_books.index(book)))

    def update_book(self):
        pass

    def list_books(self):
        return self.available_books + self.borrow_books

    def add_user(self, user):
        if isinstance(user, User):
            self.users.append(user)

    def delete_user(self, user):
        if isinstance(user, User):
            self.users.append(user)

    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "available_books": self.available_books,
            "borrow_books": self.borrow_books,
        }

    @classmethod
    def from_dict(cls, data):
        library = cls(
            name=data["name"],
            address=data["address"]
        )
        library.available_books = data["available_books"]
        library.borrow_books = data["borrow_books"]

        return library

    def __str__(self):
        return (
            f"Library: {self.name}\nAddress: {self.address}"
            f"\nAvailable books: {self.available_books}\nBorrow books: {self.borrow_books}"
            f"\nHistory books: {self.history_book} "
        )


if __name__ == "__main__":
    library = Library("Georges Pompidou ", "Paris")
    book1 = Book("Les 7 habitudes des gens qui", "Covey", "978-22902060582")
    book2 = Book("Le petit prince", "Antoine de Saint-Exupéry", "978-22902060582")
    library.add_book(book1)
    library.add_book(book2)
    library.borrow_book(book1)
    library.return_book(book1)
    print(library)




from models.paper_book import PaperBook
from models.digital_Book import DigitalBook
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
            cls._instance.history_user = {}
        return cls._instance

    def add_paper_book(self, book):
        if isinstance(book, PaperBook):
            self.available_books.append(book.to_dict())
            self.history_book[book.to_dict()["title"]] = 0

    def add_digital_book(self, book):
        if isinstance(book, DigitalBook):
            self.available_books.append(book.to_dict())
            self.history_book[book.to_dict()["title"]] = 0

    def delete_book(self, book):
        self.available_books.remove(book)

    def borrow_book(self, book, user):
        self.borrow_books.append(self.available_books.pop(self.available_books.index(book)))
        self.history_book[book["title"]] += 1
        self.history_user[user["name"]] += 1
        return self.borrow_books

    def return_book(self, book):
        self.available_books.append(self.borrow_books.pop(self.borrow_books.index(book)))
        return self.available_books

    def update_book_title(self, book, title):
        for book_ in self.available_books:
            if book_ == book:
                book_["title"] = title
                break
        return self.available_books

    def update_book_author(self, book, author):
        for book_ in self.available_books:
            if book_ == book:
                book_["author"] = author
                break
        return self.available_books

    def update_book_isbn(self, book, isbn):
        for book_ in self.available_books:
            if book_ == book:
                book_["isbn"] = isbn
                break
        return self.available_books

    def update_book_summary(self, book, summary):
        for book_ in self.available_books:
            if book_ == book:
                book_["summary"] = summary
                break
        return self.available_books

    def get_all_books(self):
        return self.available_books + self.borrow_books

    def get_all_users(self):
        return self.users

    def get_history_books(self):
        return self.history_book

    def get_history_users(self):
        return self.history_user

    def add_user(self, user):
        if isinstance(user, User):
            self.users.append(user.to_dict())
            self.history_user[user.to_dict()["name"]] = 0

    def delete_user(self, user):
        if isinstance(user, User):
            self.users.append(user)

    def to_dict(self):
        return {"name": self.name,
                "address": self.address,
                "available_books": self.available_books,
                "borrow_books": self.borrow_books,
                "history_book": self.history_book,
                "users": self.users,
                "history_user": self.history_user}

    @classmethod
    def from_dict(cls, data):
        library = cls(name=data["name"],
                      address=data["address"])
        library.available_books = data["available_books"]
        library.borrow_books = data["borrow_books"]
        library.users = data["users"]
        library.history_book = data["history_book"]
        library.history_user = data["history_user"]
        return library

    def __str__(self):
        return (
            f"Library: {self.name}\nAddress: {self.address}"
            f"\nAvailable books: {self.available_books}\nBorrow books: {self.borrow_books}"
            f"\nHistory books: {self.history_book}\nUsers: {self.users }"
        )


if __name__ == "__main__":
    pass




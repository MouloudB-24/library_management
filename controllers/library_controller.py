from models.library import Library
from others.data_management import save_library, load_library


class LibraryController:
    def __init__(self):
        self.library = load_library()

    def create_library(self, name, address):
        """
        Create a library.

        :param name: The name of the library.
        :param address: The address of library.
        """
        library = Library(name, address)
        self.library = library
        save_library(self.library)

    def add_user_to_library(self, user):
        """
        Add a user to the library.
        :param user: The user bas been to the library
        return: True if the user was successfully added, False if the library was not found.
        """
        self.library.add_user(user)
        return save_library(self.library)

    def delete_user_from_library(self, user):
        self.library.users.remove(user)
        return save_library(self.library)

    def delete_book_from_library(self, book):
        self.library.available_books.remove(book)
        return save_library(self.library)

    def find_user_by_membership_no(self, membership_no):
        for user in self.library.users:
            if user["membership_no"] == membership_no:
                return user
        return

    def find_book_by_isbn(self, isbn):
        all_books = self.library.available_books + self.library.borrow_books
        for book in all_books:
            if book["isbn"] == isbn:
                if book in self.library.available_books:
                    status = "Available"
                    return book, status
                status = "Borrowed"
                return book, status
        return None, "Not found"

    def get_all_books(self):
        return self.library.get_all_books()

    def get_history_books(self):
        return self.library.get_history_books()

    def get_history_users(self):
        return self.library.get_history_users()

    def get_all_users(self):
        return self.library.get_all_users()

    def add_paper_book_to_library(self, book):
        """
        Add a book to the library.
        :param book: The book bas been to the library
        return: True if the book was successfully added, False if the library was not found.
        """
        self.library.add_paper_book(book)
        return save_library(self.library)

    def add_digital_book_to_library(self, book):
        """
        Add a book to the library.
        :param book: The book bas been to the library
        return: True if the book was successfully added, False if the library was not found.
        """
        self.library.add_digital_book(book)
        return save_library(self.library)

    def borrow_book(self, book, user):
        self.library.borrow_book(book, user)
        return save_library(self.library)

    def return_book(self, book):
        self.library.return_book(book)
        return save_library(self.library)

    def update_book_title(self, book, information):
        self.library.available_books = self.library.update_book_title(book, information)
        return save_library(self.library)

    def update_book_author(self, book, information):
        self.library.available_books = self.library.update_book_author(book, information)
        return save_library(self.library)

    def update_book_isbn(self, book, information):
        self.library.available_books = self.library.update_book_isbn(book, information)
        return save_library(self.library)

    def update_book_summary(self, book, information):
        self.library.available_books = self.library.update_book_summary(book, information)
        return save_library(self.library)





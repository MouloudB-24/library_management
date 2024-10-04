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
        """
        self.library.add_user(user)
        return save_library(self.library)

    def delete_user_from_library(self, user):
        """
        Delete user from the library.
        """
        self.library.users.remove(user)
        return save_library(self.library)

    def add_paper_book_to_library(self, book):
        """
        Add a paper book to the library.
        """
        self.library.add_paper_book(book)
        return save_library(self.library)

    def add_digital_book_to_library(self, book):
        """
        Add a digital book to the library.
        """
        self.library.add_digital_book(book)
        return save_library(self.library)

    def delete_book_from_library(self, book):
        """
        Delete book from the library.
        """
        self.library.available_books.remove(book)
        return save_library(self.library)

    def get_all_books(self):
        """
        Obtain the list of books.
        """
        return self.library.get_all_books()

    def get_history_books(self):
        """
        Obtain a history of book borrowings.
        """
        return self.library.get_history_books()

    def get_history_users(self):
        """
        Obtain user borrowings history.
        """
        return self.library.get_history_users()

    def get_all_users(self):
        """
        Obtain the list of users.
        """
        return self.library.get_all_users()

    def borrow_book(self, book, user):
        """
        Borrow a book from the library.
        """
        self.library.borrow_book(book, user)
        return save_library(self.library)

    def return_book(self, book):
        """
        Return a book to the library.
        """
        self.library.return_book(book)
        return save_library(self.library)

    def update_book_title(self, book, title):
        """
        Update a book title.
        """
        self.library.available_books = self.library.update_book_title(book, title)
        return save_library(self.library)

    def update_book_author(self, book, author):
        """
        Update a book author.
        """
        self.library.available_books = self.library.update_book_author(book, author)
        return save_library(self.library)

    def update_book_isbn(self, book, isbn):
        """
        Update a book isbn.
        """
        self.library.available_books = self.library.update_book_isbn(book, isbn)
        return save_library(self.library)

    def update_book_summary(self, book, summary):
        """
        Update a book summary.
        """
        self.library.available_books = self.library.update_book_summary(book, summary)
        return save_library(self.library)

    def find_user_by_membership_no(self, membership_no):
        """
        Find a user by membership number.
        """
        for user in self.library.users:
            if user["membership_no"] == membership_no:
                return user
        return

    def find_book_by_isbn(self, isbn):
        """
        Find a book by ISBN.
        """
        all_books = self.library.available_books + self.library.borrow_books
        for book in all_books:
            if book["isbn"] == isbn:
                if book in self.library.available_books:
                    status = "Available"
                    return book, status
                status = "Borrowed"
                return book, status
        return None, "Not found"





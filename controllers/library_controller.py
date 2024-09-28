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

    def find_library_by_name(self, name):
        """
        Retrieve the library.
        return: Object representing the library.
        """
        if self.library.name == name:
            return self.library
        return None

    def add_user_to_library(self, user):
        """
        Add a user to the library.
        :param user: The user bas been to the library
        return: True if the user was successfully added, False if the library was not found.
        """
        self.library.users.append(user.to_dict())
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
        for book in self.library.available_books:
            if book["isbn"] == isbn:
                return book
        return

    def add_book_to_library(self, book):
        """
        Add a book to the library.
        :param book: The book bas been to the library
        return: True if the book was successfully added, False if the library was not found.
        """
        self.library.available_books.append(book.to_dict())
        return save_library(self.library)

    def get_top_borrowed_books(self):
        pass




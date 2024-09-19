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
        self.library.append(library)
        save_library(self.library)

    def retrieve_library(self):
        """
        Retrieve the library.
        return: Object representing the library.
        """
        return self.library

    def add_user_to_library(self, user):
        """
        Add a user to the library.
        :param user: The user bas been to the library
        return: True if the user was successfully added, False if the library was not found.
        """
        if self.library:
            self.library.append(user)
            save_library(self.library)
            return True
        return False

    def add_book_to_library(self, book):
        """
        Add a book to the library.
        :param book: The book bas been to the library
        return: True if the book was successfully added, False if the library was not found.
        """
        if self.library:
            self.library.append(book) # voir si ce n'est pas self.library.books.append(book)
            save_library(self.library)
            return True
        return False

    def get_top_borrowed_books(self):
        pass




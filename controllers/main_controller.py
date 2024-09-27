from controllers.user_controller import UserController
from controllers.book_controller import BookController
from controllers.library_controller import LibraryController
from views.user_view import UserView
from views.book_view import BookView
from views.library_view import LibraryView


class MainController:
    def __init__(self):
        self.user_controller = UserController()
        self.book_controller = BookController()
        self.library_controller = LibraryController()
        self.user_view = UserView()
        self.book_view = BookView()
        self.library_view = LibraryView()

    @staticmethod
    def get_user_choice():
        return input("Enter your choice 👉: ")

    def main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Manage library")
            print("2. Statistics")
            print("3. Exit")

            choice = self.get_user_choice()

            if choice == "3":
                print("Goodbye 👋")
                return
            elif choice == "1":
                self.manage_library()
            elif choice == "3":
                self.generate_statistics()
            else:
                print("Invalid choice 🤔. Please try again!")

    # --- Create library ---
    def manage_library(self):
        options = ["a. Create library", "b. Add user", "c. Add book", "d. Delete user", "e. Delete book",
                   "f. Update user", "g. Update book", "h. Search user", "i. Search book", "j. Borrow book",
                   "k. Return book", "l. List users", "m. List books", "n. Back to main menu"]
        while True:
            for option in options:
                print(option)

            choice = self.get_user_choice()

            if choice.lower() == "a":
                self.create_library()
            elif choice.lower() == "b":
                self.add_user()
            elif choice.lower() == "c":
                self.add_book()
            elif choice.lower() == "d":
                self.delete_user()
            elif choice.lower() == "e":
                self.delete_book()
            elif choice.lower() == "f":
                self.update_user()
            elif choice.lower() == "g":
                self.update_book()
            elif choice.lower() == "h":
                self.search_user()
            elif choice.lower() == "i":
                self.search_book()
            elif choice.lower() == "j":
                self.borrow_book()
            elif choice.lower() == "k":
                self.return_book()
            elif choice.lower() == "l":
                self.get_list_users()
            elif choice.lower() == "m":
                self.get_list_book()
            elif choice.lower() == "n":
                return
            else:
                print("Invalid choice 🤔. Please try again!")

    def create_library(self):
        try:
            name, address = self.library_view.get_library_details()
            self.library_controller.create_library(name, address)
            print("Library created successfully 👏")

        except Exception as e:
            print(f"Error creating library: {e}")

    def add_user(self):
        try:
            name, membership_no = self.user_view.get_user_details()
            # ... Ajouter des fonctions de validate de doonées !!

            self.user_controller.add_user(name, membership_no)
            print("The user is successfully added 👏")

        except Exception as e:
            print(f"Error adding user ‼️: {e}")

    def delete_user(self):
        try:
            membership_no = self.user_view.get_user_membership_no()
            self.user_controller.delete_user(membership_no)
            print("The user is successfully deleted 👏")
        except Exception as e:
            print(f"Error suppression user ‼️: {e}")

    def update_user(self):
        pass

    def get_list_users(self):
        pass

    def add_book(self):
        title, author, isbn, summary = self.book_view.get_book_details()
        # Ajouter des fonction de validation ...

        self.book_controller.add_book(title, author, isbn, summary)
        print("The book is successfully added 👏")

    def search_book(self):
        isbn = self.book_view.get_isbn_book()
        book = self.book_controller.find_book_by_isbn(isbn)
        if book:
            print(book)
        else:
            print("Book not found 🤗")

    def delete_book(self):
        isbn = self.book_view.get_isbn_book()
        book = self.book_controller.find_book_by_isbn(isbn)
        if book:
            self.book_controller.delete_book(book)
            print("The book is successfully deleted 👏")
        else:
            print("Book not found 🤗")

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def get_list_book(self):
        books = self.book_controller.list_books()
        if books:
            self.book_view.display_books(books)
        else:
            print("No books available 😲")

    # --- Statistics management ---
    def generate_statistics(self):
        pass


if __name__ == "__main__":
    pass


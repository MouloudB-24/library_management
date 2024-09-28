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
        # Création de la bibliothèque
        self.create_library()

        options = ['Manage menu library 👇:', '1. Add user', '2. Add book', '3. Delete user', '4. Delete book', '5. Update user',
                   '6. Update book', '7. Search user', '8. Search book', '9. Borrow book', '10. Return book',
                   '11. List users', '12. List books', '13. Back to main menu']

        while True:
            for option in options:
                print(option)

            choice = self.get_user_choice()

            if choice.lower() == "1":
                self.add_user()
            elif choice.lower() == "2":
                self.add_book()
            elif choice.lower() == "3":
                self.delete_user()
            elif choice.lower() == "4":
                self.delete_book()
            elif choice.lower() == "5":
                self.update_user()
            elif choice.lower() == "6":
                self.update_book()
            elif choice.lower() == "7":
                self.search_user()
            elif choice.lower() == "8":
                self.search_book()
            elif choice.lower() == "9":
                self.borrow_book()
            elif choice.lower() == "10":
                self.return_book()
            elif choice.lower() == "11":
                self.get_list_users()
            elif choice.lower() == "12":
                self.get_list_book()
            elif choice.lower() == "13":
                return
            else:
                print("Invalid choice 🤔. Please try again!")

    def create_library(self):
        try:
            if self.library_controller.library:
                return
            name, address = self.library_view.get_library_details()
            self.library_controller.create_library(name, address)
            print("Library successfully updated  👏")

        except Exception as e:
            print(f"Error create library: {e}")

    def add_user(self):
        try:
            name, membership_no = self.user_view.get_user_details()
            # ... Ajouter des fonctions de validate de doonées !!

            # Créer le user
            user = self.user_controller.add_user(name, membership_no)
            # Ajouter le user
            self.library_controller.add_user_to_library(user)
            print("The user is successfully added 👏")

        except Exception as e:
            print(f"Error adding user: {e}")

    def add_book(self):
        try:
            title, author, isbn, summary = self.book_view.get_book_details()
            # Ajouter des fonction de validation ...

            book = self.book_controller.add_book(title, author, isbn, summary)
            self.library_controller.add_book_to_library(book)
            print("The book is successfully added 👏")
        except Exception as e:
            print(f"Error adding book: {e}")

    def delete_user(self):
        try:
            membership_no = self.user_view.get_user_membership_no()
            user = self.library_controller.find_user_by_membership_no(membership_no)
            if user:
                self.library_controller.delete_user_from_library(user)
                print("The user is successfully deleted 👏")
            else:
                print("The user not found!")

        except Exception as e:
            print(f"Error suppression user: {e}")

    def delete_book(self):
        try:
            isbn = self.book_view.get_isbn_book()
            book = self.library_controller.find_book_by_isbn(isbn)
            if book:
                self.library_controller.delete_book_from_library(book)
                print("The book is successfully deleted 👏")
            else:
                print("The book not found!")

        except Exception as e:
            print(f"Error suppression book: {e}")

    def update_user(self):
        pass

    def update_book(self):
        pass

    def get_list_users(self):
        pass

    def search_book(self):
        isbn = self.book_view.get_isbn_book()
        book = self.book_controller.find_book_by_isbn(isbn)
        if book:
            print(book)
        else:
            print("Book not found 🤗")

    def search_user(self):
        pass

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


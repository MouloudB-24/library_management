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

    def main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Manage users")
            print("2. Manage books")
            print("3. Statistics")
            print("4. Exit")

            choice = input("Enter your choice 👉: ")

            if choice == "1":
                self.manage_users()
            elif choice == "2":
                self.manage_books()
            elif choice == "3":
                self.generate_statistics()
            elif choice == "4":
                print("Goodbye 👋")
                return
            else:
                print("Invalid choice 🤔. Please try again!")

    # --- user management ---
    def manage_users(self):
        pass

    # --- Book management ---
    def manage_books(self):
        while True:
            print("\n--- Main Books ---")
            print("1. Add a book")
            print("2. Delete a book")
            print("3. Search for book")
            print("4. Borrow a book")
            print("5. Return a book")
            print("6. List books")
            print("7. Back to main menu")

            choice = input("Enter your choice 👉: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.delete_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.borrow_book()
            elif choice == "5":
                self.return_book()
            elif choice == "6":
                self.get_list_book()
            elif choice == "7":
                return
            print("Invalid choice 🤔. Please try again!")

    def add_book(self):
        pass

    def delete_book(self):
        pass

    def add_books(self):
        pass

    def search_book(self):
        pass

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def get_list_book(self):
        pass

    # --- Statistics management ---
    def generate_statistics(self):
        pass




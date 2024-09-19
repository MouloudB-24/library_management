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

    def manage_users(self):
        pass


    def generate_statistics(self):
        pass




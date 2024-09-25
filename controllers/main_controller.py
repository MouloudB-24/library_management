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
            print("1. Manage users")
            print("2. Manage books")
            print("3. Statistics")
            print("4. Exit")

            choice = self.get_user_choice()

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
        while True:
            print("\n--- Manage users ---")
            print("1. Add user")
            print("2. Delete user")
            print("3. Update user")
            print("5. List users")
            print("6. Back to main menu")

            choice = self.get_user_choice()
            if choice == "1":
                self.add_user()
            elif choice == "2":
                self.delete_user()
            elif choice == "3":
                self.update_user()
            elif choice == "4":
                self.get_list_users()
            elif choice == "6":
                return
            else:
                print("Invalid choice 🤔. Please try again!")

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

            choice = self.get_user_choice()
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
        title, author, isbn, summary = self.book_view.get_book_details()
        # Ajouter des fonction de validation ...

        self.book_controller.add_book(title, author, isbn, summary)
        print("The book is successfully added 👏")

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


if __name__ == "__main__":
    pass


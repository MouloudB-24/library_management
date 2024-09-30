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
            print(" 1 -> Manage library")
            print(" 2 -> Statistics")
            print(" q -> Exit")

            choice = self.get_user_choice()

            if choice .lower() == "q":
                print("Goodbye 👋")
                return
            elif choice == "1":
                self.manage_library()
            elif choice == "2":
                self.generate_statistics()
            else:
                print("Invalid choice 🤔. Please try again!")

    # --- Create library ---
    def manage_library(self):
        # Create the library
        self.create_library()

        # Menu options
        options = ['---\nManage menu library 👇:', ' 1 -> Add user', ' 2 -> Delete user', ' 3 -> Add book',
                   ' 4 -> Delete book', ' 5 -> Update book', ' 6 -> Search book', ' 7 -> Borrow book',
                   ' 8 -> Return book', ' q -> Back to main menu']

        while True:
            for option in options:
                print(option)

            choice = self.get_user_choice()

            if choice.lower() == "1":
                self.add_user()
            elif choice.lower() == "2":
                self.delete_user()
            elif choice.lower() == "3":
                self.add_book()
            elif choice.lower() == "4":
                self.delete_book()
            elif choice.lower() == "5":
                self.update_book()
            elif choice.lower() == "6":
                self.search_book()
            elif choice.lower() == "7":
                self.borrow_book()
            elif choice.lower() == "8":
                self.return_book()
            elif choice.lower() == "q":
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
            user = self.user_controller.create_user(name, membership_no)
            # Ajouter le user
            self.library_controller.add_user_to_library(user)
            print("The user is successfully added 👏")

        except Exception as e:
            print(f"Error adding user: {e}")

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

    def add_book(self):
        try:
            title, author, isbn, summary, typer = self.book_view.get_book_details()
            # Ajouter des fonction de validation ...
            if typer.lower() == "paper":
                book = self.book_controller.create_paper_book(title, author, isbn, summary, typer)
                self.library_controller.add_paper_book_to_library(book)
            else:
                book = self.book_controller.create_digital_book(title, author, isbn, summary, typer)
                self.library_controller.add_digital_book_to_library(book)
            print("The book is successfully added 👏")
        except Exception as e:
            print(f"Error adding book: {e}")

    def delete_book(self):
        try:
            book, status = self._get_book_status()
            if book and status == "Available":
                self.library_controller.delete_book_from_library(book)
                print("The book is successfully deleted 👏")
            else:
                print(f"Book status: {status}")

        except Exception as e:
            print(f"Error suppression book: {e}")

    def update_book(self):
        book, status = self._get_book_status()
        if book:
            while True:
                print("what do you want to update : \n1- Title\n2- Author\n3- ISBN\n4- Summary")
                choice = input("Enter your choice: ")
                if choice.isdigit() and choice in ["1", "2", "3", "4"]:
                    break
            if choice == "1":
                title = self.book_view.get_book_title()
                self.library_controller.update_book_title(book, title)
            elif choice == "2":
                author = self.book_view.get_book_author()
                self.library_controller.update_book_author(book, author)
            elif choice == "3":
                isbn = self.book_view.get_book_isbn()
                self.library_controller.update_book_isbn(book, isbn)
            else:
                summary = self.book_view.get_book_summary()
                self.library_controller.update_book_summary(book, summary)
            print("The book is successfully updated!")

        else:
            print(f"Book status: {status}")

    def search_book(self):
        book, status = self._get_book_status()
        if book:
            self.book_view.display_book(book)
        print(f"Book status: {status}")

    def borrow_book(self):
        book, status = self._get_book_status()
        membership_no = self.user_view.get_user_membership_no()
        user = self.library_controller.find_user_by_membership_no(membership_no)
        if user:
            if status != "Available":
                print(f"Book status: {status}")
                return
            self.library_controller.borrow_book(book, user)
            print("Book successfully borrowed")
        else:
            print("The user not found!")

    def return_book(self):
        book, status = self._get_book_status()
        if status != "Borrowed":
            print(f"Book status: {status}")
            return
        self.library_controller.return_book(book)
        print("Book successfully borrowed")

    def _get_book_status(self):
        isbn = self.book_view.get_book_isbn()
        book, status = self.library_controller.find_book_by_isbn(isbn)
        return book, status

    # --- Statistics management ---
    def generate_statistics(self):
        # Statistics management menu
        options = ['---\nStatistics management menu👇:', ' 1 -> List all books', ' 2 -> List all users',
                   ' 3 -> Most borrowed books', ' 4 -> Most active users', ' q -> Back to main menu']

        while True:
            for option in options:
                print(option)

            choice = self.get_user_choice()

            if choice.lower() == "1":
                self.get_all_books()
            elif choice.lower() == "2":
                self.get_all_users()
            elif choice.lower() == "3":
                self.get_top_books()
            elif choice.lower() == "4":
                self.get_top_users()
            elif choice.lower() == "q":
                return
            else:
                print("Invalid choice 🤔. Please try again!")

    def get_all_books(self):
        books = self.library_controller.get_all_books()
        if books:
            self.book_view.display_books(books)
        else:
            print("No books available 😲")

    def get_all_users(self):
        users = self.library_controller.get_all_users()
        if users:
            self.user_view.display_users(users)
        else:
            print("No users available 😲")

    def get_top_books(self):
        books = self.library_controller.get_history_books()
        sorted_books = sorted(books.items(), key=lambda item: item[1], reverse=True)
        print("Rating of most borrowed books:")
        for rank, (title, value) in enumerate(sorted_books, start=1):
            print(f"{rank} - {title} ({value} borrowings)")

    def get_top_users(self):
        users = self.library_controller.get_history_users()
        sorted_users = sorted(users.items(), key=lambda item: item[1], reverse=True)
        print("Rating of most active users:")
        for rank, (name, value) in enumerate(sorted_users, start=1):
            print(f"{rank} - {name} - ({value} borrowings)")


if __name__ == "__main__":
    pass


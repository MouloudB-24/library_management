from controllers.user_controller import UserController
from controllers.book_controller import BookController
from controllers.library_controller import LibraryController
from views.user_view import UserView
from views.book_view import BookView
from views.library_view import LibraryView
import typer


class MainController:
    def __init__(self):
        self.user_controller = UserController()
        self.book_controller = BookController()
        self.library_controller = LibraryController()
        self.user_view = UserView()
        self.book_view = BookView()
        self.library_view = LibraryView()

    def initialize_library(self):
        library = self.library_controller.library
        if not library:
            typer.echo("You must first create a library please🤗")
            self.create_library()
        else:
            self.library_view.display_libray(library)

    def create_library(self):
        if self.library_controller.library:
            typer.secho("A library exists")
            self.library_view.display_libray(self.library_controller.library)
            return
        name, address = self.library_view.get_library_details()
        self.library_controller.create_library(name, address)
        typer.secho("Library successfully updated  👏", fg=typer.colors.GREEN, bold=True)

    def add_user(self):
        name, membership_no = self.user_view.get_user_details()
        if self._is_exist_membership_no(membership_no):
            return
        user = self.user_controller.create_user(name, membership_no)
        self.library_controller.add_user_to_library(user)
        typer.secho("The user is successfully added 👏", fg=typer.colors.GREEN, bold=True)

    def delete_user(self):
        membership_no = self.user_view.get_user_membership_no()
        user = self.library_controller.find_user_by_membership_no(membership_no)
        if user:
            typer.confirm("Do you really to delete the user?", abort=True)
            self.library_controller.delete_user_from_library(user)
            typer.secho("The user is successfully deleted 👏", fg=typer.colors.GREEN, bold=True)
        else:
            typer.secho("The user not found!", fg=typer.colors.RED, bold=True)

    def add_book(self):
        title, author, isbn, summary, typer_ = self.book_view.get_book_details()
        self._is_valid_isbn(isbn)
        book, status = self.library_controller.find_book_by_isbn(isbn)
        if self.is_exist_book(status):
            return
        self._is_valid_typer(typer_)

        if typer_ == "paper":
            book = self.book_controller.create_paper_book(title, author, isbn, summary, typer_)
            self.library_controller.add_paper_book_to_library(book)
        else:
            book = self.book_controller.create_digital_book(title, author, isbn, summary, typer_)
            self.library_controller.add_digital_book_to_library(book)
        typer.secho("The book is successfully added 👏", fg=typer.colors.GREEN, bold=True)

    def delete_book(self):
        book, status = self._get_book_status()
        if book and status == "Available":
            typer.confirm("Do you really to delete the book?", abort=True)
            self.library_controller.delete_book_from_library(book)
            typer.secho("The book is successfully deleted 👏", fg=typer.colors.GREEN, bold=True)
        else:
            typer.secho(f"Book status: {status}", fg=typer.colors.RED, bold=True)

    def update_book(self):
        book, status = self._get_book_status()
        if book:
            choice = self.ask_user()
            if choice == "1":
                title = self.book_view.get_book_title()
                self.library_controller.update_book_title(book, title)
            elif choice == "2":
                author = self.book_view.get_book_author()
                self.library_controller.update_book_author(book, author)
            elif choice == "3":
                isbn = self.book_view.get_book_isbn()
                self._is_valid_isbn(isbn)
                self.library_controller.update_book_isbn(book, isbn)
            else:
                summary = self.book_view.get_book_summary()
                self.library_controller.update_book_summary(book, summary)
            typer.secho("The book is successfully updated!", fg=typer.colors.GREEN, bold=True)

        else:
            typer.secho(f"Book status: {status}", fg=typer.colors.RED, bold=True)

    def search_book(self):
        book, status = self._get_book_status()
        if book:
            self.book_view.display_book(book)
            typer.secho(f"Book status: {status}", fg=typer.colors.GREEN, bold=True)
        else:
            typer.secho(f"Book status: {status}", fg=typer.colors.RED, bold=True)

    def borrow_book(self):
        book, status = self._get_book_status()
        membership_no = self.user_view.get_user_membership_no()
        user = self.library_controller.find_user_by_membership_no(membership_no)
        if user:
            if status != "Available":
                typer.secho(f"Book status: {status}", fg=typer.colors.RED, bold=True)
                return
            self.library_controller.borrow_book(book, user)
            typer.secho("Book successfully borrowed", fg=typer.colors.GREEN, bold=True)
        else:
            typer.secho("The user not found!", fg=typer.colors.RED, bold=True)

    def return_book(self):
        book, status = self._get_book_status()
        if status != "Borrowed":
            typer.secho(f"Book status: {status}", fg=typer.colors.RED, bold=True)
            return
        self.library_controller.return_book(book)
        typer.secho("Book successfully borrowed", fg=typer.colors.GREEN, bold=True)

    def get_all_books(self):
        books = self.library_controller.get_all_books()
        if books:
            self.book_view.display_books(books)
        else:
            typer.secho("No books available 😲", fg=typer.colors.RED, bold=True)

    def get_all_users(self):
        users = self.library_controller.get_all_users()
        if users:
            self.user_view.display_users(users)
        else:
            typer.secho("No users available 😲", fg=typer.colors.RED, bold=True)

    def get_top_books(self):
        books = self.library_controller.get_history_books()
        sorted_books = sorted(books.items(), key=lambda item: item[1], reverse=True)
        typer.secho("Rating of most borrowed books:", bold=True)
        for rank, (title, value) in enumerate(sorted_books, start=1):
            typer.secho(f"{rank} - {title} ({value} borrowings)", bold=True)

    def get_top_users(self):
        users = self.library_controller.get_history_users()
        sorted_users = sorted(users.items(), key=lambda item: item[1], reverse=True)
        typer.secho("Rating of most active users:", bold=True)
        for rank, (name, value) in enumerate(sorted_users, start=1):
            typer.secho(f"{rank} - {name} - ({value} borrowings)", bold=True)

    @staticmethod
    def is_exist_book(status):
        if status != "Not found":
            typer.secho("A book with the same ISBN exists in the library!", fg=typer.colors.RED, bold=True)
            return True
        return False

    @staticmethod
    def get_user_choice():
        return typer.prompt("Enter your choice 👉")

    @staticmethod
    def ask_user():
        while True:
            typer.secho("What do you want to update : \n1- Title\n2- Author\n3- ISBN\n4- Summary", bold=True)
            choice = typer.prompt("Enter your choice")
            if choice.isdigit() and choice in ["1", "2", "3", "4"]:
                return choice

    def _is_exist_membership_no(self, membership_no):
        if self.library_controller.find_user_by_membership_no(membership_no):
            typer.secho("A user with the same membership_no exists in the library!", fg=typer.colors.RED, bold=True)
            return True
        return False

    def _get_book_status(self):
        isbn = self.book_view.get_book_isbn()
        book, status = self.library_controller.find_book_by_isbn(isbn)
        return book, status

    def _is_valid_isbn(self, isbn):
        while not self.book_controller.is_valid_isbn(isbn):
            typer.secho("The ISBN must be a sequence of numbers 😡", fg=typer.colors.RED, bold=True)
            isbn = self.book_view.get_book_isbn()

    def _is_valid_typer(self, typer_):
        while not self.book_controller.is_valid_typer_(typer_):
            typer.secho("The typer is 'paper' or 'digital' 😡", fg=typer.colors.RED, bold=True)
            typer_ = self.book_view.get_book_typer_()


if __name__ == "__main__":
    pass


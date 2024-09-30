import typer
from controllers.main_controller import MainController

app = typer.Typer()
controller = MainController()


@app.command()
def run():
    """
    Command to start library management.
    """
    controller.main_menu()


@app.command()
def add_user():
    """
    Command to add a user.
    """
    controller.add_user()


@app.command()
def delete_user():
    """
    Command to delete a user.
    """
    controller.delete_user()


@app.command()
def add_book():
    """
    Command to add a book.
    """
    controller.add_book()


@app.command()
def delete_book():
    """
    Command to delete a book.
    """
    controller.delete_book()


@app.command()
def update_book():
    """
    Command to update a book.
    """
    controller.update_book()


@app.command()
def search_book():
    """
    Command to search a book.
    """
    controller.search_book()


@app.command()
def borrow_book():
    """
    Command to borrow a book.
    """
    controller.borrow_book()


@app.command()
def return_book():
    """
    Command to return a book.
    """
    controller.return_book()


@app.command()
def all_books():
    """
    Command to get all books.
    """
    controller.get_all_books()


@app.command()
def all_books():
    """
    Command to get all users.
    """
    controller.get_all_users()


@app.command()
def top_books():
    """
    Command to get top books.
    """
    controller.get_top_books()


@app.command()
def top_users():
    """
    Command to get top users.
    """
    controller.get_top_users()


if __name__ == "__main__":
    app()
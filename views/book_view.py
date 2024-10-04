import typer


class BookView:
    @staticmethod
    def display_book(book):
        """
        Display the details of book.
        """
        typer.secho(f"Title: {book.get('title')}", bold=True)
        typer.secho(f"Author: {book.get('author')}", bold=True)
        typer.secho(f"ISBN: {book.get('isbn')}", bold=True)
        typer.secho(f"Summary: {book.get('summary')}", bold=True)

    @staticmethod
    def display_books(books):
        """
        Display a list of books.
        """
        if not books:
            typer.secho("No books available 🤗", bold=True)
        else:
            for book in books:
                typer.secho(f"{book['title']} - {book['author']} (ISBN: {book['isbn']})", bold=True)

    @staticmethod
    def get_book_details():
        """
        Prompts the user for book details.
        """
        title = typer.prompt("Enter title: ")
        author = typer.prompt("Enter author: ")
        isbn = typer.prompt("Enter ISBN: ")
        summary = typer.prompt("Enter summary: ")
        typer_ = typer.prompt("Enter typer (paper/digital): ")
        return title, author, isbn, summary, typer_

    @staticmethod
    def get_book_isbn():
        """
        Prompts the user for the book's ISBN.
        """
        return typer.prompt("Enter book's ISBN")

    @staticmethod
    def get_book_title():
        """
        Prompts the user for the book's title.
        """
        return typer.prompt("Enter book's title")

    @staticmethod
    def get_book_author():
        """
        Prompts the user for the book's author.
        """
        return typer.prompt("Enter book's author: ")

    @staticmethod
    def get_book_summary():
        """
        Prompts the user for the book's summary.
        """
        return typer.prompt("Enter book's summary")

    @staticmethod
    def get_book_typer_():
        """
        Prompts the user for the book's typer.
        """
        return typer.prompt("Enter book's typer (paper or digital): ")


from models.paper_book import PaperBook
from models.digital_Book import DigitalBook


class BookController:
    def __init__(self):
        self.paper_book_model = PaperBook
        self.digital_book_model = DigitalBook

    def create_paper_book(self, title, author, isbn, summary, typer):
        """
        Create a paper book.
        """
        return self.paper_book_model(title, author, isbn, summary, typer)

    def create_digital_book(self, title, author, isbn, summary, typer):
        """
        Create a digital book.
        """
        return self.digital_book_model(title, author, isbn, summary, typer)

    def is_valid_isbn(self, isbn):
        return isbn.isdigit()

    def is_valid_typer_(self, typer_):
        typer_ = typer_.lower()
        return typer_ in ["paper", "digital"]


from models.paper_book import PaperBook
from models.digital_Book import DigitalBook


class BookController:
    def __init__(self):
        self.paper_book_model = PaperBook
        self.digital_book_model = DigitalBook

    def create_paper_book(self, title, author, isbn, summary, typer):
        return self.paper_book_model(title, author, isbn, summary, typer)

    def create_digital_book(self, title, author, isbn, summary, typer):
        return self.digital_book_model(title, author, isbn, summary, typer)


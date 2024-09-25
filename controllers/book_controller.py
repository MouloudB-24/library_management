from models.book import Book
from others.data_management import save_books, load_books


class BookController:
    def __init__(self):
        self.books = load_books()

    def add_book(self, title, author, isbn, summary):
        book = Book(title, author, isbn, summary)
        # ... Générer le cas ou le book existe déjà
        self.books.append(book)
        save_books(self.books)

    def list_books(self):
        return self.books

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return

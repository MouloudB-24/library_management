from models.book import Book


class DigitalBook(Book):
    def __init__(self, title=None, author=None, isbn=None, summary=None, type="digital"):
        super().__init__(title, author, isbn, summary)
        self.type = type

    def __str__(self):
        return f"{super().__str__()}\nType: {self.type}"

    def to_dict(self):
        book = super().to_dict()
        book["type"] = self.type
        return book

class Book:
    def __init__(self, title=None, author=None, isbn=None):
        """
        Initializes a new book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_isbn(self, isbn):
        self.isbn = isbn

    def to_dict(self):
        """
        Converts the book information to dictionary.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a book from dictionary.

        :param data: Dictionary containing the book data.
        """
        return cls(
            title=data["title"],
            author=data["author"],
            isbn=data["isbn"],
        )

    def __str__(self):
        """
        return a string representation of the book.
        """
        return f"Title: {self.title} - Author: {self.author} - ISBN: {self.isbn}"


class DigitalBook(Book):
    def __init__(self, title=None, author=None, isbn=None, type="Digital"):
        super().__init__(title, author, isbn)
        self.type = type

    def __str__(self):
        return f"{super().__str__()} Type: {self.type}"


class PaperBook(Book):
    def __init__(self, title=None, author=None, isbn=None, type="Paper"):
        super().__init__(title, author, isbn)
        self.type = type

    def __str__(self):
        return f"{super().__str__()} Type: {self.type}"


if __name__ == "__main__":
    book = Book("Les 7 habitudes des gens qui", "Covey", "978-22902060582")
    print(book)
    book_d = DigitalBook()
    print(book_d)
    book_p = PaperBook()
    print(book_p)


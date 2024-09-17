class Book:
    def __init__(self, title=None, author=None, isbn=None, type=None):
        """
        Initializes a new book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.type = type

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_type(self, type):
        self.type = type

    def to_dict(self):
        """
        Converts the book information to dictionary.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "type": self.type,
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
            type=data["type"],
        )

    def __str__(self):
        """
        return a string representation of the book.
        """
        return f"Title: {self.title} - Author: {self.author} - ISBN: {self.isbn} - Type: {self.type}"


if __name__ == "__main__":
    book = Book("Les 7 habitudes des gens qui", "Covey", "978-22902060582", "D")
    data = book.to_dict()
    print(book.from_dict(data))

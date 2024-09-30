class Book:
    def __init__(self, title=None, author=None, isbn=None, summary=None):
        """
        Initializes a new book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.summary = summary

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_summary(self, summary):
        self.summary = summary

    def to_dict(self):
        """
        Converts the book information to dictionary.
        """
        return {"title": self.title,
                "author": self.author,
                "isbn": self.isbn,
                "summary": self.summary}

    @classmethod
    def from_dict(cls, data):
        """
        Creates a book from dictionary.

        :param data: Dictionary containing the book data.
        """
        return cls(title=data["title"],
                   author=data["author"],
                   isbn=data["isbn"],
                   summary=data["summary"])

    def __str__(self):
        """
        return a string representation of the book.
        """
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nSummary: {self.summary}"


if __name__ == "__main__":
    pass
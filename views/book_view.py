class BookView:
    @staticmethod
    def display_book(book):
        """
        Display the details of book.
        """
        print(f"Title: {book.get('title')}")
        print(f"Author: {book.get('author')}")
        print(f"ISBN: {book.get('isbn')}")
        print(f"Summary: {book.get('summary')}")

    @staticmethod
    def display_books(books):
        """
        Display a list of books.
        """
        if not books:
            print("No books available 🤗")
        else:
            for book in books:
                print(f"{book['title']} - {book['author']} (ISBN: {book['isbn']})")

    @staticmethod
    def get_book_details():
        """
        Prompts the user for book details.
        """
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        summary = input("Enter summary: ")
        typer = input("Enter typer (paper/digital): ")
        return title, author, isbn, summary, typer

    @staticmethod
    def get_book_isbn():
        """
        Prompts the user for the book's ISBN.
        """
        return input("Enter book's ISBN: ")

    @staticmethod
    def get_book_title():
        """
        Prompts the user for the book's title.
        """
        return input("Enter book's title: ")

    @staticmethod
    def get_book_author():
        """
        Prompts the user for the book's author.
        """
        return input("Enter book's author: ")

    @staticmethod
    def get_book_summary():
        """
        Prompts the user for the book's summary.
        """
        return input("Enter book's summary: ")

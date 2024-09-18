class BookView:
    @staticmethod
    def display_book(book):
        """
        Display the details of book.
        """
        print(f"Title: {book.name}")
        print(f"Author: {book.author}")
        print(f"ISBN: {book.isbn}")
        print(f"Summary: {book.summary}")

    @staticmethod
    def display_books(books):
        """
        Display a list of books.
        """
        if not books:
            print("No books available 🤗")
        else:
            for book in books:
                print(f"{book.title} - {book.author} (ISBN: {book.isbn})")

    @staticmethod
    def get_book_details():
        """
        Prompts the user for book details.
        """
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        summary = input("Enter summary: ")
        return title, author, isbn, summary

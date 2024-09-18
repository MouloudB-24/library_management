class LibraryView:
    @staticmethod
    def display_library(library):
        """
        Display the details of library.
        """
        print(f"Library name: {library.name}")
        print(f"Address: {library.address}")
        print(f"Available books: {library.available_books}")
        print(f"Borrow books: {library.borrow_books}")

    @staticmethod
    def get_library_details():
        """
        Prompts the user for library details.
        """
        name = input("Enter library name: ")
        address = input("Enter library address: ")
        return name, address

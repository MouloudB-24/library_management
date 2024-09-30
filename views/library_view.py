class LibraryView:

    @staticmethod
    def get_library_details():
        """
        Prompts the user for library details.
        """
        name = input("Enter library name: ")
        address = input("Enter library address: ")
        return name, address

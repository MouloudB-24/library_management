import typer


class LibraryView:

    @staticmethod
    def get_library_details():
        """
        Prompts the user for library details.
        """
        name = typer.prompt("Enter library name: ")
        address = typer.prompt("Enter library address: ")
        return name, address

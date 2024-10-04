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

    @staticmethod
    def display_libray(library):
        """
        Display the details of libray.
        """
        typer.secho(f"{library.name} - {library.address}", fg=typer.colors.GREEN, bg=typer.colors.BLACK, bold=True)


import typer


class UserView:
    @staticmethod
    def display_user(user):
        """
        Display the details of user.
        """
        typer.secho(f"Name: {user.name}", bold=True)
        typer.secho(f"Membership no: {user.membership_no}", bold=True)

    @staticmethod
    def display_users(users):
        """
        Display a list of users.
        """
        if not users:
            typer.secho("No registered users 🤗", fg=typer.colors.RED, bold=True)
        else:
            for user in users:
                typer.secho(f"{user['name']}  (Membership no: {user['membership_no']})", bold=True)

    @staticmethod
    def get_user_details():
        """
        prompts the user to provide information.
        """
        name = typer.prompt("Enter name: ")
        membership_no = typer.prompt("Enter membership number")
        return name, membership_no

    @staticmethod
    def get_user_membership_no():
        """
        Asks user for membership number.
        """
        return typer.prompt("Enter user's membership number")


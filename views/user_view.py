class UserView:
    @staticmethod
    def display_user(user):
        """
        Display the details of user.
        """
        print(f"Name: {user.name}")
        print(f"Membership number: {user.membership_no}")

    @staticmethod
    def display_users(users):
        """
        Display a list of users.
        """
        if not users:
            print("No registered users 🤗")
        else:
            for user in users:
                print(f"{user['name']} (Membership number: {user['membership_no']})")

    @staticmethod
    def get_user_details():
        """
        prompts the user to provide information.
        """
        name = input("Enter name: ")
        membership_no = input("Enter membership number: ")
        return name, membership_no

    @staticmethod
    def get_user_membership_no():
        """
        Asks user for membership number.
        """
        return input("Enter membership number :")


class User:
    def __init__(self, name=None, membership_no=None):
        """
        Initialize a new user.
        """
        self.name = name
        self.membership_no = membership_no

    def set_name(self, name):
        self.name = name

    def set_membership_no(self, membership_no):
        self.membership_no = membership_no

    def to_dict(self):
        """
        Converts the user information to dictionary.
        """
        return {
            "name": self.name,
            "membership_no": self.membership_no,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a user from dictionary.

        :param data: Dictionary containing the user data
        """
        return cls(
            name=data["name"],
            membership_no=data["membership_no"],
        )

    def __str__(self):
        return f"{self.name} - MEMBERSHIP_NO: {self.membership_no}"


if __name__ == "__main__":
    pass
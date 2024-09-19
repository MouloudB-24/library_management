from models.user import User
from others.data_management import save_users, load_users


class UserController:
    def __init__(self):
        self.users = load_users()

    def add_user(self, name, membership_no):
        user = User(name, membership_no)
        # ... Générer le cas ou le user existe déjà
        self.users.append(user)
        save_users(self.users)

    def delete_user(self, membership_no):
        user = self.find_user_by_membership_no(membership_no)
        if user:
            self.users.remove()
        return

    def find_user_by_membership_no(self, membership_no):
        for user in self.users:
            if user.membership_no == membership_no:
                return user
        return


    def list_users(self):
        return self.users



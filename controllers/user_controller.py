from models.user import User
from others.data_management import save_users, load_users


class UserController:
    def __init__(self):
        self.users = load_users()

    def add_user(self, name, membership_no):
        return User(name, membership_no)

    def list_users(self):
        return self.users



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

    def list_users(self):
        return self.users



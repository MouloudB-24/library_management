from models.user import User


class UserController:
    def __init__(self):
        self.user_model = User

    def create_user(self, name, membership_no):
        return self.user_model(name, membership_no)



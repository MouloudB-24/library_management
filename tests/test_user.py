from models.user import User
import pytest


@pytest.fixture
def user():
    return User("Aylan", "0001A")


def test_user_creation(user):
    assert user.name == "Aylan"
    assert user.membership_no == "0001A"


def test_user_to_dict(user):
    user_dict = {"name": "Aylan", "membership_no": "0001A"}
    assert user.to_dict() == user_dict


def test_user_from_dict(user):
    user_dict = {"name": "Aylan", "membership_no": "0001A"}
    user_ = user.from_dict(user_dict)
    assert user_.name == "Aylan"
    assert user_.membership_no == "0001A"

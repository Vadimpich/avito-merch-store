from app.db.models import User
from app.db.repository.user_repo import get_user_by_username, create_user
from conftests import *


def test_create_user(db):
    """Тест создания пользователя"""
    user = create_user(db, "mynewuser", "hashedpassword")
    assert user is not None
    assert user.username == "mynewuser"


def test_get_user_by_username(db):
    """Тест поиска пользователя"""
    db.add(User(username="findme", hashed_password="hashed"))
    db.commit()

    user = get_user_by_username(db, "findme")
    assert user is not None
    assert user.username == "findme"

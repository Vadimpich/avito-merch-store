from app.db.repository.user_repo import get_user_by_username
from app.services.auth_service import authenticate_or_register_user
from conftests import *


@pytest.mark.usefixtures("db")
def test_register_user(db):
    """Тестируем автоматическую регистрацию нового пользователя"""
    username = "newuser"
    password = "testpassword"

    token = authenticate_or_register_user(db, username, password)

    user = get_user_by_username(db, username)
    assert user is not None
    assert user.username == username
    assert len(token) > 10


@pytest.mark.usefixtures("db")
def test_login_existing_user(db):
    """Тестируем вход существующего пользователя"""
    username = "existinguser"
    password = "testpassword"

    authenticate_or_register_user(db, username,
                                  password)
    token = authenticate_or_register_user(db, username, password)

    assert len(token) > 10

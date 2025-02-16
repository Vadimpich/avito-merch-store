from datetime import timedelta

from fastapi import status
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from app.core.exceptions import CustomHTTPException
from app.core.security import (hash_password, verify_password,
                               create_access_token)
from app.db.repository.user_repo import get_user_by_username, create_user


def authenticate_or_register_user(db: Session, username: str,
                                  password: str) -> str:
    user = get_user_by_username(db, username)

    if not user:
        try:
            hashed_password = hash_password(password)
            user = create_user(db, username, hashed_password)
        except IntegrityError:
            db.rollback()
            user = get_user_by_username(db, username)

    elif not verify_password(password, user.hashed_password):
        raise CustomHTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                  message="Неверные учётные данные")

    access_token = create_access_token(data={"sub": str(user.id)},
                                       expires_delta=timedelta(minutes=30))
    return access_token

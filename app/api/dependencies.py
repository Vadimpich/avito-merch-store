from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.exceptions import CustomHTTPException
from app.core.security import decode_access_token
from app.db.repository.user_repo import get_user_by_id
from app.db.session import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = CustomHTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        message="Не предоставлены учётные данные",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception

    user_id: int = payload.get("sub")
    user = get_user_by_id(db, user_id)
    if user is None:
        raise credentials_exception

    return user

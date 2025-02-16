import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.api.dependencies import get_db
from app.db.session import Base
from fastapi.testclient import TestClient
from app.main import app

# Подключение к тестовой SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False,
                                   bind=engine)


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    """Создаёт тестовую БД перед всеми тестами"""
    Base.metadata.create_all(
        bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db():
    """Создаёт новую сессию БД для каждого теста"""
    session = TestingSessionLocal()
    yield session
    session.close()


@pytest.fixture(scope="function")
def client(db):
    """Создаёт тестовый клиент FastAPI и использует `db`"""

    def override_get_db():
        yield db

    app.dependency_overrides[
        get_db] = override_get_db  # ✅ Обновляем зависимость

    return TestClient(app)

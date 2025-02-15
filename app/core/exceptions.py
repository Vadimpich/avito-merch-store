from fastapi import HTTPException


class CustomHTTPException(HTTPException):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code=status_code, detail=None)  # detail удаляем
        self.errors = message  # Ошибку добавляем в `errors`

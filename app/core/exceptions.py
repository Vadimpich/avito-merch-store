from fastapi import HTTPException


class CustomHTTPException(HTTPException):
    def __init__(self, status_code: int, message: str, headers: dict = None):
        super().__init__(status_code=status_code, detail=None, headers=headers)
        self.errors = message

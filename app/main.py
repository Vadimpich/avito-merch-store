from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api import router
from app.core.exceptions import CustomHTTPException

app = FastAPI(title="Avito Merch Store")
app.include_router(router, prefix="/api")


@app.exception_handler(CustomHTTPException)
async def custom_http_exception_handler(request: Request, exc: CustomHTTPException):
    return JSONResponse(status_code=exc.status_code, content={"errors": exc.errors})


@app.get("/")
def root():
    return {"message": "Avito Merch Store"}

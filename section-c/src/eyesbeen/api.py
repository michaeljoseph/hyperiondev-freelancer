"""eyesbeen api layer"""
from fastapi import FastAPI

from eyesbeen import validate_isbn

app = FastAPI()


@app.get("/isbn/{isbn}")
def read_isbn_validation(isbn: str):
    """Validate and convert to isbn13"""
    return {"result": validate_isbn(isbn)}

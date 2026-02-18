

from fastapi import APIRouter


router = APIRouter(prefix="", tags=["home"])

@router.get("/")
def root():
    return {"message": "Hello world"}


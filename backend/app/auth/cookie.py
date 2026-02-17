

from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session
from jose import JWTError

from database import get_db
from models import User
from .token import decode_token



cookie_name = "access_token"

def get_user(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get(cookie_name)
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        user_id = decode_token(token)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def set_auth_cookie(response, token: str):
    response.set_cookie(
        key=cookie_name,
        value=token,
        httponly=True,
        secure=False,  
        samesite="lax",
        path="/",
    )

def clear_auth_cookie(response):
    response.delete_cookie(key=cookie_name, path="/")



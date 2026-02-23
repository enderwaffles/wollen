

from fastapi import APIRouter, Depends, HTTPException, Response, Form
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import User
from schemas.user import UserSignup, UserLogin, VerifyIn, UserForgot, UserForgot2
from dotenv import load_dotenv
import os

from auth.token import create_token, decode_token
from auth.hash import hash_password, verify_password
from auth.cookie import get_user, set_auth_cookie, clear_auth_cookie
from auth.mail import sendcode


router = APIRouter(prefix="", tags=["authentication"])
load_dotenv()


@router.post("/make_admin")
def make_admin(db: Session = Depends(get_db),
               user: User = Depends(get_user)
               ):
    admin = "enderwaffles2004@gmail.com"
    print(user.email)
    print(admin)
    # obj = db.query(User).filter(User.id == user.id).first()

    if not user.email == admin:
        raise HTTPException(status_code=403)
    
    user.admin = True
    db.commit()
    
    return {"message": "You are admin", "user": user, "admin": admin}

@router.get("/protected")
def protected(user: User = Depends(get_user)):
    return {
        "message": "access free",
        "user": user
    }

@router.post("/signup", status_code=201)
def signup(data: UserSignup, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == data.name).first()
    if user and user.is_verified:
        raise HTTPException(status_code=400, detail="User already is")
    
    hashed_password = hash_password(data.password)
    code = sendcode(data.email) 


    obj = User(email=data.email, 
            nickname=data.nickname, 
            name=data.name.capitalize(),
            surname=data.surname.capitalize(), 
            password=hashed_password,
            is_verified=False,
            email_code=code)
    db.add(obj)

    db.commit()
    db.refresh(obj)
    return {"message": "sent code"}



@router.post("/verify")
def verify(data: VerifyIn, response: Response, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if user.email_code != data.code:
        raise HTTPException(status_code=400, detail="Wrong code")
    
    user.is_verified = True
    user.email_code = None
    db.commit()

    token = create_token(user.id)
    set_auth_cookie(response, token)

    return {"message": "logged in", "token_type": "cookie", "user": user}

@router.post("/login")
def login(data: UserLogin, response: Response, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="wrong name or password")

    if not user.is_verified:
        raise HTTPException(status_code=403, detail="Email not verified")

    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="wrong name or password")

    token = create_token(user.id)
    set_auth_cookie(response, token)

    return {"message": "logged in", "token_type": "cookie", "user": user}

@router.post("/logout")
def logout(response: Response):
    clear_auth_cookie(response)
    return {"message": "logged out"}

@router.post("/forgot1")
def forgot1(data: UserForgot, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404)
    
    hashed_password = hash_password(data.new_password)
    code = sendcode(data.email)
    user.reset_code=code
    user.new_password=hashed_password
    db.commit()
    db.refresh(user)

    return {"message": "code sent"}

@router.post("/forgot2")
def forgot2(data: UserForgot2, response: Response, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if user.reset_code != data.code:
        raise HTTPException(status_code=400, detail="Wrong code")
    
    user.password=user.new_password
    user.reset_code=None
    user.new_password=None
    db.commit()
    db.refresh(user)

    token = create_token(user.id)
    set_auth_cookie(response, token)

    return {"message": "logged in", "token_type": "cookie", "user": user}



from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    email: str
    nickname: str
    name: str
    surname: str

    class Config:
        from_attributes = True

class UserSignup(BaseModel):
    email: str
    nickname: str
    name: str
    surname: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class VerifyIn(BaseModel):
    email: str
    code: str

class UserForgot(BaseModel):
    email: str
    new_password: str

class UserForgot2(BaseModel):
    email: str
    code: str

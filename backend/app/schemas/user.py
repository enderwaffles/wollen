

from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    nickname: str
    name: str
    surname: str

    class Config:
        from_attributes = True

class UserSignup(BaseModel):
    email: EmailStr
    nickname: str
    name: str
    surname: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class VerifyIn(BaseModel):
    email: EmailStr
    code: str

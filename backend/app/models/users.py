

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"sqlite_autoincrement": True} 
    id = Column(Integer, primary_key=True)
    email = Column(String(96), nullable=False, unique=True, index=True)
    nickname = Column(String(24), nullable=False, unique=True, index=True)
    name = Column(String(24), nullable=False)
    surname = Column(String(24), nullable=False)
    password = Column(String(256), nullable=False) #hashed by werkzeug
    avatar_url = Column(String(512), nullable=True) #profile picture  
    admin = Column(Boolean, default=False)
    
    is_verified = Column(Boolean, default=False)
    email_code = Column(String(4), nullable=True)
    reset_code = Column(String(4), default=None, nullable=True)
    new_password = Column(String(256), default=None, nullable=True)


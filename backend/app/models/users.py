

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
    password = Column(String(256), nullable=False) 
    isadmin = Column(Boolean, default=False, nullable=False) 
    
    is_verified = Column(Boolean, default=False)
    email_code = Column(String(4), nullable=True)
    


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {"sqlite_autoincrement": True}

    id = Column(Integer, primary_key=True)

    title = Column(String(120), nullable=False, unique=True)
    slug = Column(String(140), nullable=False, unique=True, index=True)
    
    products = relationship("Product", back_populates="category", cascade="all, delete")

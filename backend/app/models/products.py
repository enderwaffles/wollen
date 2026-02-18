

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Numeric, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class Product(Base):
    __tablename__ = "products"
    __table_args__ = {"sqlite_autoincrement": True} 

    id = Column(Integer, primary_key=True)

    title = Column(String(32), nullable=False)
    description = Column(String(128), nullable=True)

    upload_url = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.utcnow)
    
    price = Column(Numeric(10, 2), nullable=False)
    # currency = Column(String(3), nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="products")


    
    



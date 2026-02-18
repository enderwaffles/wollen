
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductResponse(BaseModel):
    id: int
    title: str
    description: str
    upload_url: Optional[str] = None    
    date: datetime
    price: float
    category_id: int

    class Config:
        from_attributes = True

class AddProduct(BaseModel):
    title: str
    description: str
    # upload_url: Optional[str] = None    
    price: float
    category_id: int





from pydantic import BaseModel
from .product import ProductResponse


class CategoryResponse(BaseModel):
    id: int
    title: str
    slug: str
    products: ProductResponse

class AddCategory(BaseModel):
    title: str
    slug: str



from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from database import get_db
from models import Product, Category

from schemas.product import ProductResponse, AddProduct
from schemas.category import CategoryResponse, AddCategory

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/categories")
def categories(db: Session = Depends(get_db)):
    obj = db.query(Category).all()
    return obj

@router.get("/categories/{id}")
def category(id: int, db: Session = Depends(get_db)):
    obj = db.query(Category).options(
        joinedload(Category.products)
        ).filter(Category.id == id).first()
    
    if not obj:
        raise HTTPException(status_code=404)
    return obj


@router.get("/")
def products(db: Session = Depends(get_db)):
    obj = db.query(Product).all()
    return obj

@router.get("/{id}")
def product(id: int, db: Session = Depends(get_db)):
    obj = db.query(Product).filter(Product.id == id).first()
    if not obj:
        raise HTTPException(status_code=404)
    return obj


@router.post("/categories")
def add_category(data: AddCategory, db: Session = Depends(get_db)):
    obj = Category(**data.model_dump()) 
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.post("/")
def add_product(data: AddProduct, db: Session = Depends(get_db)):
    obj = Product(**data.model_dump()) 
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    obj = db.query(Product).filter(Product.id == id).first()
    if not obj:
        raise HTTPException(status_code=404)
    db.delete(obj)
    db.commit()
    return None


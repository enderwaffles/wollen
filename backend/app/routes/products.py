

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session, joinedload
from typing import Optional
import os
from datetime import datetime

from database import get_db
from models import Product, Category

from schemas.product import ProductResponse, AddProduct
from schemas.category import CategoryResponse, AddCategory

from auth import User, get_user


router = APIRouter(prefix="/products", tags=["products"])

@router.get("/categories")
def categories(db: Session = Depends(get_db)):
    obj = db.query(Category).all()
    return obj

@router.get("/categories/{slug}")
def category(slug: str, db: Session = Depends(get_db)):
    obj = db.query(Category).options(
        joinedload(Category.products)
        ).filter(Category.slug == slug).first()
    
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
def add_category(data: AddCategory, 
                 db: Session = Depends(get_db),
                 user: User = Depends(get_user)
                 ):
    
    if not user.isadmin:
        raise HTTPException(status_code=403)

    obj = Category(**data.model_dump()) 
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.post("/")
def add_product(title: str = Form(...), 
                description: str = Form(...), 
                price: float = Form(...), 
                category_id: int = Form(...),
                file: Optional[UploadFile] = File(None),
                db: Session = Depends(get_db),
                user: User = Depends(get_user)
                ):
    
    if not user.isadmin:
        raise HTTPException(status_code=403)

    obj = Product(title=title,
                  description=description,
                  price=price,
                  category_id=category_id,
                  ) 
    
    db.add(obj)
    db.commit()
    db.refresh(obj)

    if file is not None:
        os.makedirs("static", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f") 
        name = f"{obj.id}_{obj.title}_{timestamp}_{file.filename}"
        disk_path = f"static/{name}"
        with open(disk_path, "wb") as f:
            f.write(file.file.read())
        obj.upload_url = disk_path
        db.commit()
        db.refresh(obj)

    return obj


@router.delete("/{id}")
def delete_product(id: int, 
                   db: Session = Depends(get_db),
                   user: User = Depends(get_user)
                   ):
    
    if not user.isadmin:
        raise HTTPException(status_code=403)

    obj = db.query(Product).filter(Product.id == id).first()
    if not obj:
        raise HTTPException(status_code=404)
    
    db.delete(obj)
    db.commit()
    return None


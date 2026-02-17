

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker



database_url = "sqlite:///./block.db" 
engine = create_engine(database_url, connect_args={"check_same_thread": False})

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():  
    db = SessionLocal()
    try: yield db
    finally: db.close()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)


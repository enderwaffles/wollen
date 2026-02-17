
#FastAPI
from fastapi import FastAPI
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

from database import init_db
init_db()

from routes import routers
for router in routers:
    app.include_router(router)



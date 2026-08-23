from fastapi import FastAPI

from app.database import engine, Base
from app import models
from app.router import auth
from app.router import transactions


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(transactions.router)



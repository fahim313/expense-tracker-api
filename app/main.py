from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from app.database import engine, Base
from app import models
from router import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Expense Tracker API"}
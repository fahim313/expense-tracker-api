from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from app.database import engine, Base
from app import models


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Expense Tracker API"}
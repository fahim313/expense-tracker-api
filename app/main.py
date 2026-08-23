from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Expense Tracker API"}
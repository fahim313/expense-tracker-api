from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated, Optional
 
from app.database import get_db
from app.models import Transaction, User
from app.schemas import (
    TransactionCreate,
    TransactionUpdate,
    TransactionResponse
)
from app.auth_utils import get_current_user
 
 
router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)
 
 
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[User, Depends(get_current_user)]


# 1. CREATE TRANSACTION


@router.post("/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
def create_transaction(transaction_data: TransactionCreate, db: db_dependency, current_user: user_dependency):
    transaction_model = Transaction(
        title=transaction_data.title,
        amount=transaction_data.amount,
        type=transaction_data.type,
        category=transaction_data.category,
        date=transaction_data.date,
        owner_id=current_user.id
    )

    db.add(transaction_model)
    db.commit()
    db.refresh(transaction_model)

    return transaction_model

 
# 2. READ ALL TRANSACTIONS

@router.get("/", response_model=list[TransactionResponse])
def get_transactions(db: db_dependency, current_user: user_dependency):
    transactions = db.query(Transaction).filter(
        Transaction.owner_id == current_user.id
    ).all()

    return transactions

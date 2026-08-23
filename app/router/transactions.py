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


# Create Transaction


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

 
#  Get All Transaction 

@router.get("/", response_model=list[TransactionResponse])
def get_transactions(db: db_dependency, current_user: user_dependency):
    transactions = db.query(Transaction).filter(
        Transaction.owner_id == current_user.id
    ).all()

    return transactions 


# Filter Transaction

@router.get( "/filter",response_model=list[TransactionResponse])
def filter_transactions(
    db: db_dependency,
    current_user: user_dependency,
    type: Optional[str] = None,
    category: Optional[str] = None,
    minimum_amount: Optional[float] = None,
    maximum_amount: Optional[float] = None
):
    query = db.query(Transaction).filter(
        Transaction.owner_id == current_user.id
    )

    if type is not None:
        query = query.filter(Transaction.type == type)

    if category is not None:
        query = query.filter(Transaction.category == category)

    if minimum_amount is not None:
        query = query.filter(Transaction.amount >= minimum_amount)

    if maximum_amount is not None:
        query = query.filter(Transaction.amount <= maximum_amount)

    return query.all()

# Get Transaction By ID 

@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(transaction_id: int, db: db_dependency, current_user: user_dependency):
    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.owner_id == current_user.id
    ).first()

    if transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

    return transaction

# Update Transaction 

@router.put("/{transaction_id}", response_model=TransactionResponse)
def update_transaction(
    transaction_id: int,
    transaction_data: TransactionUpdate,
    db: db_dependency,
    current_user: user_dependency
):
    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.owner_id == current_user.id
    ).first()

    if transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

    update_data = transaction_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(transaction, key, value)

    db.commit()
    db.refresh(transaction)

    return transaction


#  Delete Transaction 

@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, db: db_dependency, current_user: user_dependency):
    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.owner_id == current_user.id
    ).first()

    if transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

    db.delete(transaction)
    db.commit()

    return {"message": "Transaction deleted successfully"}
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Literal
from datetime import date as Date 


# User Schemas

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6)


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)



# Transaction Schemas

class TransactionCreate(BaseModel):
    title: str
    amount: float = Field(gt=0)
    type: Literal["income", "expense"]
    category: str
    date: Date


class TransactionUpdate(BaseModel):
    title: str | None = None
    amount: float | None = Field(default=None, gt=0)
    type: Literal["income", "expense"] | None = None
    category: str | None = None
    date: Date | None = None


class TransactionResponse(BaseModel):
    id: int
    title: str
    amount: float
    type: str
    category: str
    date: Date
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
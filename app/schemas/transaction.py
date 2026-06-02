from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.transaction import TransactionType

class TransactionCreate(BaseModel):
    title: str
    amount: float
    type: TransactionType
    description: Optional[str] = None
    date: datetime
    category_id: Optional[int] = None

class TransactionUpdate(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = None
    type: Optional[TransactionType] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
    category_id: Optional[int] = None

class TransactionResponse(BaseModel):
    id: int
    title: str
    amount: float
    type: TransactionType
    description: Optional[str] = None
    date: datetime
    user_id: int
    category_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
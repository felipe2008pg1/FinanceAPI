from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from app.db.database import get_db
from app.schemas.transaction import TransactionCreate, TransactionUpdate, TransactionResponse
from app.models.transaction import TransactionType
from app.services.transaction_service import (
    create_transaction, get_transactions, get_transaction_by_id,
    update_transaction, delete_transaction
)
from app.api.v1.endpoints.auth import get_current_user_dep

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/", response_model=TransactionResponse, status_code=201)
def create(data: TransactionCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user_dep)):
    return create_transaction(db, data, current_user.id)

@router.get("/", response_model=List[TransactionResponse])
def list_transactions(
    skip: int = 0,
    limit: int = 20,
    type: Optional[TransactionType] = None,
    category_id: Optional[int] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user_dep)
):
    return get_transactions(db, current_user.id, skip, limit, type, category_id, start_date, end_date)

@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_one(transaction_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user_dep)):
    return get_transaction_by_id(db, transaction_id, current_user.id)

@router.put("/{transaction_id}", response_model=TransactionResponse)
def update(transaction_id: int, data: TransactionUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user_dep)):
    return update_transaction(db, transaction_id, current_user.id, data)

@router.delete("/{transaction_id}", status_code=204)
def delete(transaction_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user_dep)):
    delete_transaction(db, transaction_id, current_user.id)
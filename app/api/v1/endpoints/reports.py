from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
from app.db.database import get_db
from app.services.transaction_service import get_summary, get_by_category
from app.api.v1.endpoints.auth import get_current_user_dep

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/summary")
def summary(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user_dep)
):
    return get_summary(db, current_user.id, start_date, end_date)

@router.get("/by-category")
def by_category(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user_dep)
):
    results = get_by_category(db, current_user.id, start_date, end_date)
    return [
        {
            "category_id": r.category_id,
            "type": r.type,
            "total": r.total
        }
        for r in results
    ]
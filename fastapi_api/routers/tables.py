from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from database import get_db
from models import TableModel

router = APIRouter(
    tags=["Tables"]
)


@router.get("/tables")
def get_tables(
    branch_id: int,
    party_size: int,
    db: Session = Depends(get_db)
):

    tables = db.query(
        TableModel
    ).filter(
        TableModel.branch_id == branch_id,
        TableModel.seating_capacity >= party_size,
        TableModel.is_active == True
    ).all()

    return tables
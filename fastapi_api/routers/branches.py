from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from database import get_db
from models import RestaurantBranch

router = APIRouter(
    tags=["Branches"]
)


@router.get("/branches")
def get_branches(
        db: Session = Depends(get_db)
):

    branches = db.query(
        RestaurantBranch
    ).all()

    return branches
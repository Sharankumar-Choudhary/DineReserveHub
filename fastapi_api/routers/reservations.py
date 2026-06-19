from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database import get_db

from models import Reservation
from models import TableModel

from schemas import ReservationCreate
from datetime import timedelta
from datetime import datetime
from oauth2 import get_current_user

router = APIRouter(
    tags=["Reservations"]
)

@router.post("/reservations")
def create_reservation(
    request: ReservationCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    table = db.query(TableModel).filter(
        TableModel.id == request.table_id
    ).first()

    if not table:
        raise HTTPException(
            status_code=404,
            detail="Table not found"
        )

    if table.seating_capacity < request.party_size:
        raise HTTPException(
            status_code=400,
            detail="Table capacity insufficient"
        )

    start_time = request.reservation_time - timedelta(hours=2)

    end_time = request.reservation_time + timedelta(hours=2)

    existing = db.query(
        Reservation
    ).filter(
        Reservation.table_id == request.table_id,
        Reservation.status == "CONFIRMED",
        Reservation.reservation_time >= start_time,
        Reservation.reservation_time <= end_time
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Table already booked in this time window"
        )

    reservation = Reservation(
    user_id=current_user["user_id"],
    table_id=request.table_id,
    reservation_time=request.reservation_time,
    party_size=request.party_size,
    status="CONFIRMED",
    created_at=datetime.utcnow()
)

    db.add(reservation)
    db.commit()

    return {
        "message": "Reservation created successfully"
    }

@router.get("/user/reservations")
def get_my_reservations(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    reservations = db.query(
        Reservation
    ).filter(
        Reservation.user_id == current_user["user_id"]
    ).all()

    return reservations

@router.patch("/reservations/{reservation_id}/cancel")
def cancel_reservation(
    reservation_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    reservation = db.query(
        Reservation
    ).filter(
        Reservation.id == reservation_id
    ).first()

    if not reservation:
        raise HTTPException(
            status_code=404,
            detail="Reservation not found"
        )

    if reservation.user_id != current_user["user_id"]:
        raise HTTPException(
            status_code=403,
            detail="Not authorized"
        )

    reservation.status = "CANCELLED"

    db.commit()

    return {
        "message": "Reservation cancelled successfully"
    }
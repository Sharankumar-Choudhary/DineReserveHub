from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from datetime import datetime

from sqlalchemy.orm import Session

from database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

from models import User
from schemas import UserRegister

from hashing import hash_password
from schemas import UserLogin

from hashing import verify_password

from oauth2 import create_access_token

@router.post("/register")
def register_user(
    request: UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == request.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
    name=request.name,
    email=request.email,
    role="DINER",
    password_hash=hash_password(request.password),
    created_at=datetime.utcnow()
)

    db.add(new_user)
    db.commit()

    return {
        "message": "User registered successfully"
    }

@router.post("/login")
def login_user(
    request: UserLogin,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == request.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        request.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "user_id": user.id,
            "role": user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


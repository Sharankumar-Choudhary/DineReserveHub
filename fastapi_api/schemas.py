from pydantic import BaseModel
from datetime import datetime


class UserRegister(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class ReservationCreate(BaseModel):
    table_id: int
    reservation_time: datetime
    party_size: int

from datetime import datetime

class ReservationCreate(BaseModel):
    table_id: int
    reservation_time: datetime
    party_size: int


from datetime import datetime
from pydantic import BaseModel


class ReservationResponse(BaseModel):
    id: int
    table_id: int
    reservation_time: datetime
    party_size: int
    status: str

    class Config:
        from_attributes = True
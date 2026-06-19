from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

from database import Base


class User(Base):
    __tablename__ = "users_user"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))

    email = Column(String(255), unique=True)

    role = Column(String(20))

    password_hash = Column(String(255))



    created_at = Column(DateTime)


class RestaurantBranch(Base):
    __tablename__ = "restaurants_restaurantbranch"

    id = Column(Integer, primary_key=True)

    branch_name = Column(String(100))

    address = Column(String(500))

    contact_number = Column(String(20))


class TableModel(Base):
    __tablename__ = "restaurants_tablemodel"

    id = Column(Integer, primary_key=True)

    branch_id = Column(
        Integer,
        ForeignKey("restaurants_restaurantbranch.id")
    )

    table_number = Column(String(20))

    seating_capacity = Column(Integer)

    is_active = Column(Boolean)


from sqlalchemy.sql import func

class Reservation(Base):
    __tablename__ = "reservations_reservation"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users_user.id"))

    table_id = Column(Integer, ForeignKey("restaurants_tablemodel.id"))

    reservation_time = Column(DateTime)

    party_size = Column(Integer)

    status = Column(String(20))

    created_at = Column(
        DateTime,
        server_default=func.now()
    )
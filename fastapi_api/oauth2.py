from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "dinereservehubsecretkey"
ALGORITHM = "HS256"

security = HTTPBearer()


def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
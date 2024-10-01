from datetime import datetime
from socketserver import UDPServer

from fastapi import Request, HTTPException, Depends
from jose import jwt, JWTError
from sqlalchemy.sql.functions import current_user

from config.settings import settings
from models.users import Users
from services.users_services import UsersService


def get_token(request: Request):
    token = request.cookies.get("booking_service_access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Token is missing")
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        HTTPException(status_code=401, detail="Token is invalid")
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=401, detail="Token is expired")
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="User ID is missing")
    user = await UsersService.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return  user


# async def get_current_admin_user(current_user: Users = Depends(get_current_user):
#     if current_user.role != "admin":
#         raise HTTPException(status_code=401, detail="Not admin!")
#     return current_user
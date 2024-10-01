from datetime import datetime

from fastapi import Request, HTTPException, Depends
from jose import jwt, JWTError

from config.settings import settings
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
from fastapi import Depends, Request, HTTPException
from jose import ExpiredSignatureError, JWTError, jwt

from config.settings import settings
from services.users_services import UsersService


def get_token(request: Request):
    token = request.cookies.get("booking_service_access_token")
    if not token:
        raise HTTPException(402, "Token is missing")
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except ExpiredSignatureError:
        raise HTTPException(402,"Token is expired")
    except JWTError:
        raise HTTPException(402, "Token is invalid")
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(402, "User ID is missing")
    user = await UsersService.find_one_or_none(id=int(user_id))
    if not user:
        raise HTTPException(402, "User ID is invalid")

    return user
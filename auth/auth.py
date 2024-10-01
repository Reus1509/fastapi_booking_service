from fastapi import HTTPException

from jose import jwt
from datetime import datetime, timedelta

from marshmallow.fields import Email
from passlib.context import CryptContext
from pydantic import EmailStr

from services.users_services import UsersService

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, "qwhdohqwoiduqowe@(*$Y!(Yhr", "HS256"
    )
    return encoded_jwt

def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, "<KEY>"
    )
    return encoded_jwt

async def authenticate_user(email: EmailStr, password: str):
    user = await UsersService.find_one_or_none(email=email)
    if not user and not verify_password(password, password):
        return None
    return user
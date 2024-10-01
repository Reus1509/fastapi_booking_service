from venv import create

from fastapi import APIRouter, HTTPException, Response

from auth.auth import get_password_hash, verify_password, authenticate_user, create_access_token
from services.users_services import UsersService
from shemas.users_shemas import SUserAuth

router = APIRouter(
    prefix="/users",
    tags=["Авторизация и Аутентификация"],
)

@router.post("/register")
async def register_user(user: SUserAuth):
    existing_user = await UsersService.find_one_or_none(email=user.email)
    if existing_user:
        raise HTTPException(status_code=500, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    await UsersService.add_data(email=user.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user: SUserAuth):
    user = await authenticate_user(user.email, user.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token = create_access_token({"sub": user.id})
    response.set_cookie("booking_service_access_token", access_token, httponly=True)


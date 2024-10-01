from venv import create

from fastapi import APIRouter, HTTPException, Response, Depends
from sqlalchemy.sql.functions import current_user

from auth.auth import get_password_hash, authenticate_user, create_access_token
from config.dependencies import get_current_user
from models.users import Users
from services.users_services import UsersService
from shemas.users_shemas import SUserAuth

router = APIRouter(
    prefix="/auth",
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
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_service_access_token", access_token, httponly=True)

@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_service_access_token")

@router.get("/me")
async def read_user_me(user: Users = Depends(get_current_user)):
    return user


# @router.get("/users")
# async def read_users(user: Users = Depends(get_current_admin_user)):
#     return current_user

@router.get("/all")
async def read_all_users(current_user: Users = Depends(get_current_user)):
    return await UsersService.find_all()
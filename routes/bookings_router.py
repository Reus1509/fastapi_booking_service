from fastapi import APIRouter, Request, Depends

from config.dependencies import get_current_user
from models.users import Users
from services.booking_service import BookingService
from shemas.booking_shemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)

@router.get("/")
async def bookings_get(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingService.find_all(user_id=user.id)


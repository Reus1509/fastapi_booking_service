from datetime import date

from fastapi import APIRouter, Request, Depends, HTTPException

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

@router.post("")
async def add_booking(
        room_id: int,
        date_from: date,
        date_to: date,
        user: Users = Depends(get_current_user),
):
    booking = await BookingService.add_booking(user.id, room_id, date_from, date_to)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking can't be added, all rooms are booked!")

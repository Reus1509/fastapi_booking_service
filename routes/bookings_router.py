from fastapi import APIRouter

from services.booking_service import BookingService
from shemas.booking_shemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)

@router.get("/")
async def bookings_get() -> list[SBooking]:
    return await BookingService.find_all()

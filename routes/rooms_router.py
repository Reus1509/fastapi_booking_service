from fastapi import APIRouter, Query

from datetime import date, datetime, timedelta
from typing import List

from services.rooms_service import  RoomsService
from shemas.rooms_shemas import SRoom, SRoomInfo
from routes.hotels_router import router


@router.get("/{hotel_id}/rooms")
# Этот эндпоинт можно и нужно кэшировать, но в курсе этого не сделано, чтобы
# можно было проследить разницу в работе /rooms (без кэша) и /hotels (с кэшем).
async def get_rooms_by_time(
    hotel_id: int,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
) -> List[SRoomInfo]:
    rooms = await RoomsService.find_all(hotel_id, date_from, date_to)
    return rooms

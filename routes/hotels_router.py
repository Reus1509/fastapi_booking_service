from datetime import date, datetime, timedelta
from typing import List, Optional

from fastapi import APIRouter, Query, HTTPException

from services.hotels_service import HotelsService
from shemas.hotels_shemas import SHotel, SHotelInfo

router = APIRouter(prefix="/hotels", tags=["Отели"])


@router.get("/{location}")
async def get_hotels_by_location_and_time(
    location: str,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
) -> List[SHotelInfo]:
    if date_from > date_to:
        raise HTTPException(401, detail="date_from > date_to")
    if (date_to - date_from).days > 31:
        raise HTTPException(401, detail=">31")
    hotels = await HotelsService.find_all(location, date_from, date_to)
    return hotels


@router.get("/id/{hotel_id}", include_in_schema=True)
# Этот эндпоинт используется для фронтенда, когда мы хотим отобразить все
# номера в отеле и информацию о самом отеле. Этот эндпоинт как раз отвечает за информацию
# об отеле.
# В нем нарушается правило именования эндпоинтов: конечно же, /id/ здесь избыточен.
# Тем не менее, он используется, так как эндпоинтом ранее мы уже задали получение
# отелей по их локации вместо id.
async def get_hotel_by_id(
    hotel_id: int,
) -> Optional[SHotel]:
    return await HotelsService.find_one_or_none(id=hotel_id)

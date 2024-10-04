from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from routes.hotels_router import get_hotels_by_location_and_time

router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"],
)

templates = Jinja2Templates(directory="templates")

@router.get("/hotels")
async def get_hotels_page(request: Request,
                          hotels=Depends(get_hotels_by_location_and_time)):
    return templates.TemplateResponse("hotels.html", {"request": request, "hotels": hotels})

from fastapi import UploadFile, APIRouter
import shutil

router = APIRouter(
    prefix="/images",
    tags=["Загрузка картинок"],
)

@router.post("/hotels")
async def add_hotel_image(name: int, image: UploadFile):
    with open(f"static/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(image.file, file_object)


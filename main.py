from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from routes.bookings_router import router as bookings_router
from routes.users_router import router as users_router
from routes.hotels_router import router as hotels_router
from routes.rooms_router import router as rooms_router
from routes.pages_router import router as pages_router
from routes.images_router import router as images_router
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(bookings_router)
app.include_router(users_router)
app.include_router(hotels_router)
app.include_router(rooms_router)
app.include_router(pages_router)
app.include_router(images_router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
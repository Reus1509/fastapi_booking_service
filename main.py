from fastapi import FastAPI
from routes.bookings_router import router as bookings_router
from routes.users_router import router as users_router
from routes.hotels_router import router as hotels_router
from routes.rooms_router import router as rooms_router

app = FastAPI()

app.include_router(bookings_router)
app.include_router(users_router)
app.include_router(hotels_router)
app.include_router(rooms_router)
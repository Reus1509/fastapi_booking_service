from fastapi import FastAPI
from routes.bookings_router import router as bookings_router
from routes.users_router import router as users_router

app = FastAPI()

app.include_router(bookings_router)
app.include_router(users_router)
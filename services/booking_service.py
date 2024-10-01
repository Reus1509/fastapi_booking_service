from models.bookings import Bookings
from services.base_services import BaseService


class BookingService(BaseService):
    model = Bookings
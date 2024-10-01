from models.users import Users

from services.base_services import BaseService


class UsersService(BaseService):
    model = Users

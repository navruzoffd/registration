from auth.models import Users
from src.dao.base import BaseDAO

class AuthDAO(BaseDAO):
    model = Users
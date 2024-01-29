from src.database import async_session_maker
from sqlalchemy import select
from auth.models import Users

class UsersDAO:
    @classmethod
    async def get_users(cls):
        async with async_session_maker() as session:
            query = select(Users)
            result = await session.execute(query)
            return result.mappings().all()
        
    @classmethod
    async def add_user(cls, user):
        async with async_session_maker() as session:
            query = Users(name=user.name, password=user.password)
            session.add(query)
            await session.commit()
            return f"Пользователь {user.name} добавлен"
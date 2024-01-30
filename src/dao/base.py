from src.database import async_session_maker
from sqlalchemy import select

class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, find_id):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=find_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = cls.model(**data)
            session.add(query)
            await session.commit()
            return f"Пользователь {data['name']} добавлен"
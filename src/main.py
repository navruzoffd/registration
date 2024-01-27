from fastapi import FastAPI
from src.database import async_session_maker
from sqlalchemy import select
from src.models import Users
from src.schemas import RegisterSheme

app = FastAPI()

@app.post("/registration")
async def registration(user: RegisterSheme):
    async with async_session_maker() as session:
        query = Users(name=user.name, password=user.password)
        session.add(query)
        await session.commit()
        return f'Пользователь {user.name} добавлен'


@app.get("/users")
async def get_users():
    async with async_session_maker() as session:
        query = select(Users)
        result = await session.execute(query)
        return result.scalars().all()
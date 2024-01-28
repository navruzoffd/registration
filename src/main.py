from fastapi import FastAPI
from src.schemas import RegisterSheme
from src.dao import UsersDAO

app = FastAPI()

@app.get("/users")
async def get_users():
    return await UsersDAO.get_users()

@app.post("/registration")
async def add_user(user: RegisterSheme):
        return await UsersDAO.add_user(user)
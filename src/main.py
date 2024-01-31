from fastapi import FastAPI, Depends
from src.auth.router import router as auth_router
from src.dao.usersdao import UsersDAO
from src.schemas import SUsersDB
from src.auth.dependencies import get_current_user

app = FastAPI()

app.include_router(auth_router)

@app.get("/users")
async def get_users() -> list[SUsersDB]:
    return await UsersDAO.find_all()

@app.get("/my_name")
async def get_my_name(user = Depends(get_current_user)):
    return user.name
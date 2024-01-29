from fastapi import APIRouter
from auth.dao import UsersDAO
from auth.schemas import RegisterSheme

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.get("/users")
async def get_users():
    return await UsersDAO.get_users()

@router.post("/registration")
async def add_user(user: RegisterSheme):
        return await UsersDAO.add_user(user)
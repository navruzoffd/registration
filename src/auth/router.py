from fastapi import APIRouter, Response
from src.auth.exceptions import UserIsExistException, UserLoginException
from src.dao.usersdao import UsersDAO
from src.auth.schemas import *
from src.auth.auth import get_password_hash, authenticate_user, create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post("/registration")
async def register_user(user: SRegisterUser):
    existing_user = await UsersDAO.find_one_or_none(nickname=user.nickname)
    if existing_user:
        raise UserIsExistException
    hash_password = get_password_hash(user.password)
    await UsersDAO.add(name=user.name, surname=user.surname, 
                       nickname=user.nickname, password=hash_password)
    return f"Пользователь {user.nickname} добавлен"

@router.post("/login")
async def login_user(response: Response, user_data: SLoginUser):
    user = await authenticate_user(user_data.nickname, user_data.password)
    if not user:
        raise UserLoginException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)
    return f"{user_data.nickname}, добро пожаловать"

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    return "Вы вышли"
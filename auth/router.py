from fastapi import APIRouter, HTTPException, status, Response
from auth.dao import AuthDAO
from auth.schemas import *
from auth.auth import get_password_hash, authenticate_user, create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.get("/users")
async def get_users() -> list[SUsers]:
    return await AuthDAO.find_all()

@router.post("/registration")
async def register_user(user: SRegisterUser):
    existing_user = await AuthDAO.find_one_or_none(nickname=user.nickname)
    if existing_user:
        return f"Пользователь с никнеймом {user.nickname} уже существует"
    hash_password = get_password_hash(user.password)
    await AuthDAO.add(name=user.name, surname=user.surname, 
                       nickname=user.nickname, password=hash_password)
    return f"Пользователь {user.nickname} добавлен"

@router.post("/login")
async def login_user(response: Response, user_data: SLoginUser):
    user = await authenticate_user(user_data.nickname, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": user.id})
    response.set_cookie("access_token", access_token, httponly=True)
    return f"{user_data.nickname}, добро пожаловать"
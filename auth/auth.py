from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from auth.dao import AuthDAO
from src.config import SECRET_KEY, ALGORITHM
from fastapi.concurrency import run_in_threadpool

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt



async def authenticate_user(nickname: str, password: str):
    user = await AuthDAO.find_one_or_none(nickname=nickname)
    if not user:
        return None
    # Выполнение синхронной проверки пароля в исполнителе
    password_matches = await run_in_threadpool(verify_password, password, user.password)
    if not password_matches:
        return None
    return user
    
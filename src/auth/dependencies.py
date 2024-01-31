from fastapi import Depends, Request
from jose import jwt, JWTError
from src.auth.exceptions import (TokenAbsentException, TokenExpiredException,
                                 TokenIncorrectFormatException, UserLoginException)
from src.dao.usersdao import UsersDAO
from src.config import SECRET_KEY, ALGORITHM
from datetime import datetime

def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise TokenAbsentException
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
    except JWTError:
        raise TokenIncorrectFormatException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise TokenIncorrectFormatException
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserLoginException
    
    return user
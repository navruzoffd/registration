from fastapi import HTTPException, status

UserLoginException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Пользователь отсутствует"
    )

UserIsExistException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Пользователь с таким никнеймом уже существует"
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Токен отсутствует"
    )

TokenIncorrectFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный формат токена"
    )

TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен истёк"
    )

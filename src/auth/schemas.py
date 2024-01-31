from pydantic import BaseModel

class SRegisterUser(BaseModel):
    name: str
    surname: str
    nickname: str
    password: str

class SLoginUser(BaseModel):
    nickname: str
    password: str
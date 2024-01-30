from pydantic import BaseModel

class SUsers(BaseModel):    
    id: int
    name: str
    surname: str
    nickname: str
    password: str

class SRegisterUser(BaseModel):
    name: str
    surname: str
    nickname: str
    password: str

class SLoginUser(BaseModel):
    nickname: str
    password: str
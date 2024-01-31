from pydantic import BaseModel

class SUsersDB(BaseModel):    
    id: int
    name: str
    surname: str
    nickname: str
    password: str
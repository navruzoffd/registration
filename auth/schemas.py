from pydantic import BaseModel

class RegisterSheme(BaseModel):
    name: str
    password: str
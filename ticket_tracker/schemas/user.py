from pydantic import BaseModel
from models.user_role import UserRole

class UserCreate(BaseModel):
    fullname: str
    username: str
    password: str



class UserResponse(BaseModel):
    id: int
    fullname: str
    username: str
    role: UserRole
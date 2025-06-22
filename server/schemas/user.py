from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: Optional[str] = "user"

class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(UserBase):
    user_id: int
    user_role: str

    model_config = {
        "from_attributes": True
    }

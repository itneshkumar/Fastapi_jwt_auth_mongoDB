from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    is_active: bool = False
    is_verified: bool = False
    verified_at: datetime = None
    registered_at: datetime = None
    updated_at: datetime = None
    created_at: datetime = datetime.now()

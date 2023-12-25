from users.models import UserModel
from fastapi.exceptions import HTTPException
from core.security import get_password_hash
from datetime import datetime


async def create_user_account(data, db):
    user = db.find_one({"email": data.email})
    if user:
        raise HTTPException(status_code=422, detail="Email is already registered with us.")

    new_user = UserModel(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        password=get_password_hash(data.password),
        is_active=False,
        is_verified=False,
        registered_at=datetime.now(),
        updated_at=datetime.now()
    )
    new_user=dict(new_user)
    db.insert_one(new_user)
    return new_user

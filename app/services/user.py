from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user import get_user_by_id, create_user, delete_user

def get_user_service(db: Session, user_id: int):
    return get_user_by_id(db, user_id)

def create_user_service(db: Session, user_data: dict):
    user = User(**user_data)
    return create_user(db, user)

def delete_user_service(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if user:
        return delete_user(db, user)
    return None
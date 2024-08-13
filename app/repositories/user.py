from app.utils.auth.hash_password import hash_password, verify_password
from app.schemas.auth import RegisterRequest
from sqlalchemy.orm import Session
from config.database import get_db
from app.models.user import User
from sqlalchemy import func

db: Session = next(get_db())

def create_user(request: RegisterRequest):
    try:
        hashed_password = hash_password(request.password)
        db_user = User(name=request.name ,email=request.email, password=hashed_password)
        db.add(db_user)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    
def update_user(user: User, request: RegisterRequest):
    try:
        user.name = request.name
        user.email = request.email
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    
def delete_user(user: User):
    try:
        user.deletedAt = func.now()
        db.commit()
    except Exception as e:
        raise e

def get_user_by_id(user_id: int):
    try:
        return db.query(User).filter(User.id == user_id, User.deletedAt == None).first()
    except Exception as e:
        raise e

def get_user_by_email(email: str):
    try:
        return db.query(User).filter(User.email == email, User.deletedAt == None).first()
    except Exception as e:
        raise e

def authenticate_user(email: str, password: str):
    user = get_user_by_email(email)
    if user and verify_password(password, user.password):
        return user
    return None
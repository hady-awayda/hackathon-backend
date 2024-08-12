from sqlalchemy import func
from sqlalchemy.orm import Session
from app.schemas.auth import RegisterRequest
from app.utils.auth.hash_password import hash_password, verify_password
from app.models.user import User

def create_user(db: Session, request: RegisterRequest):
    try:
        hashed_password = hash_password(request.password)
        db_user = User(name=request.name ,email=request.email, password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        raise e
    
def update_user(db: Session, user: User, request: RegisterRequest):
    try:
        user.name = request.name
        user.email = request.email
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        db.rollback()
        raise e
    
def delete_user(db: Session, user: User):
    try:
        user.deletedAt = func.now()
        db.commit()
        return user
    except Exception as e:
        raise e

def get_user_by_id(db: Session, user_id: int):
    try:
        return db.query(User).filter(User.id == user_id, User.deletedAt == None).first()
    except Exception as e:
        raise e

def get_user_by_email(db: Session, email: str):
    try:
        return db.query(User).filter(User.email == email, User.deletedAt == None).first()
    except Exception as e:
        raise e

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if user and verify_password(password, user.password):
        return user
    return None
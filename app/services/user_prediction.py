from sqlalchemy.orm import Session
from app.models.user_prediction import UserPrediction
from app.repositories.user_prediction import get_prediction_by_id, create_prediction, delete_prediction, update_prediction

def get_prediction_service(db: Session, prediction_id: int):
    return get_prediction_by_id(db, prediction_id)

def create_prediction_service(db: Session, prediction_data: dict):
    prediction = UserPrediction(**prediction_data)
    return create_prediction(db, prediction)

def update_prediction_service(db: Session, prediction_id: int, prediction_data: dict):
    prediction = get_prediction_by_id(db, prediction_id)
    if prediction:
        return update_prediction(db, prediction, prediction_data)
    return None

def delete_prediction_service(db: Session, prediction_id: int):
    prediction = get_prediction_by_id(db, prediction_id)
    if prediction:
        return delete_prediction(db, prediction)
    return None
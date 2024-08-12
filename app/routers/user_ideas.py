from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.user_prediction import create_prediction_controller, get_prediction_controller, delete_prediction_controller, update_prediction_controller
from config.database import get_db

router = APIRouter()

@router.get("/{prediction_id}")
def get_prediction(prediction_id: int, db: Session = Depends(get_db)):
    return get_prediction_controller(db, prediction_id)

@router.post("/")
def create_prediction(prediction_data: dict, db: Session = Depends(get_db)):
    return create_prediction_controller(db, prediction_data)

@router.patch("/{prediction_id}")
def update_prediction(prediction_id: int, prediction_data: dict, db: Session = Depends(get_db)):
    return update_prediction_controller(db, prediction_id, prediction_data)

@router.delete("/{prediction_id}")
def delete_prediction(prediction_id: int, db: Session = Depends(get_db)):
    return delete_prediction_controller(db, prediction_id)
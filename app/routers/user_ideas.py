from fastapi import APIRouter, Depends
from app.controllers.user_prediction import create_prediction_controller, get_prediction_controller, delete_prediction_controller, update_prediction_controller
from app.middleware.checkPaidUser import check_paid_user

router = APIRouter(
    dependencies=[Depends(check_paid_user)]
)

@router.get("/{prediction_id}")
def get_prediction(prediction_id: int):
    return get_prediction_controller(prediction_id)

@router.post("/")
def create_prediction(prediction_data: dict):
    return create_prediction_controller(prediction_data)

@router.patch("/{prediction_id}")
def update_prediction(prediction_id: int, prediction_data: dict):
    return update_prediction_controller(prediction_id, prediction_data)

@router.delete("/{prediction_id}")
def delete_prediction(prediction_id: int):
    return delete_prediction_controller(prediction_id)
from fastapi import HTTPException
from app.services.user_prediction import create_prediction_service, get_prediction_service, delete_prediction_service, update_prediction_service

def get_prediction_controller(prediction_id: int):
    try:
        prediction = get_prediction_service(prediction_id)
        if prediction is None:
            raise HTTPException(status_code=404, detail="Prediction not found")
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def create_prediction_controller(prediction_data: dict):
    try:
        return create_prediction_service(prediction_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_prediction_controller(prediction_id: int, prediction_data: dict):
    try:
        prediction = get_prediction_service(prediction_id)
        if prediction is None:
            raise HTTPException(status_code=404, detail="Prediction not found")
        return update_prediction_service(prediction, prediction_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_prediction_controller(prediction_id: int):
    try:
        prediction = delete_prediction_service(prediction_id)
        if prediction is None:
            raise HTTPException(status_code=404, detail="Prediction not found")
        return {"message": "Prediction deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
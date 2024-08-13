from app.models.user_prediction import UserPrediction
from app.repositories.user_prediction import get_prediction_by_id, create_prediction, delete_prediction, update_prediction

def get_prediction_service(prediction_id: int):
    return get_prediction_by_id(prediction_id)

def create_prediction_service(prediction_data: dict):
    prediction = UserPrediction(**prediction_data)
    return create_prediction(prediction)

def update_prediction_service(prediction: UserPrediction, prediction_data: dict):
    for key, value in prediction_data.items():
        setattr(prediction, key, value)
    return update_prediction()

def delete_prediction_service(prediction_id: int):
    prediction = get_prediction_by_id(prediction_id)
    if prediction:
        return delete_prediction(prediction)
    return None
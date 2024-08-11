from app.schemas.predict_model import PredictRequest
from app.services.random_forest import predict_success

def random_forest_controller(request: PredictRequest):
    input_series = request.model_dump()
    prediction = predict_success(input_series)
    return {"prediction": prediction}
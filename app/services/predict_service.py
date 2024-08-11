from app.ml_models.predict_model import predict_success
from app.utils.logger import logger

def predict_success_service(input_data: dict):
    try:
        prediction, tips = predict_success(input_data)
        logger.info(f"success_rate: {prediction}, tips: {tips}")
        return prediction, tips
    except Exception as e:
        logger.error(f"Error: {e}")
        raise e
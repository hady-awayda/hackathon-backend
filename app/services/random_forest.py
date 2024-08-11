from app.utils.logs.logger import logger
from app.ml_models.random_forest import make_prediction
from app.utils.helpers.generate_tips import generate_tips
from app.utils.loaders.random_forest_loader import load_prediction_model
from app.pre_processors.random_forest import prepare_input_data

def random_forest_service(input_data: dict):
    try:
        prediction, tips = predict_success(input_data)
        logger.info(f"success_rate: {prediction}, tips: {tips}")
        return prediction, tips
    except Exception as e:
        logger.error(f"Error: {e}")
        raise e
    
def predict_success(input_series: dict) -> tuple:
    try:
        model = load_prediction_model()
        test_data = prepare_input_data(input_series)
        adjusted_probability = make_prediction(model, test_data)
        tips = generate_tips(input_series, adjusted_probability)
        return adjusted_probability, tips
    except Exception as e:
        raise e
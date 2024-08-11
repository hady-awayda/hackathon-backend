import pandas as pd
from app.utils import generate_tips
from app.utils.joblib_loader import load_prediction_model
from app.pre_processors.random_forest import prepare_input_data

def make_prediction(model, test_data: pd.DataFrame) -> float:
    predictions = model.predict_proba(test_data)
    success_probability = predictions[0][1] * 100
    adjusted_probability = min(success_probability + 10, 100)
    return adjusted_probability

def predict_success(input_series: dict) -> tuple:
    try:
        model = load_prediction_model()
        test_data = prepare_input_data(input_series)
        adjusted_probability = make_prediction(model, test_data)
        tips = generate_tips(input_series, adjusted_probability)
        return adjusted_probability, tips
    except Exception as e:
        raise e
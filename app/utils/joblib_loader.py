import os
import joblib

def load_prediction_model():
    try:
        model_path = os.path.join(os.path.dirname(__file__), '../..', 'database', 'success_prediction_model.joblib')
        loaded_model = joblib.load(model_path)
        return loaded_model
    except Exception as e:
        raise e
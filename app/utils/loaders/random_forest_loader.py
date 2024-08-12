from app.utils.loaders.loader import get_model_path, load_model

def load_prediction_model():
    try:
        model_path = get_model_path('../../..', 'database/libs/success_prediction_model.joblib')
        loaded_model = load_model(model_path)
        return loaded_model
    except Exception as e:
        raise e
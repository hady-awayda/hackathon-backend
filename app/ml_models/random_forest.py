import pandas as pd

def make_prediction(model, test_data: pd.DataFrame) -> float:
    predictions = model.predict_proba(test_data)
    success_probability = predictions[0][1] * 100
    adjusted_probability = min(success_probability + 10, 100)
    return adjusted_probability
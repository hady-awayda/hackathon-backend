import os
import joblib
import pandas as pd
from pathlib import Path

def get_model_path(*relative_paths: str) -> str:
    return os.path.join(os.path.dirname(__file__), *relative_paths)

def load_model(model_path: str):
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        raise e

def load_datasets(csv_path: str, csv_reviews_path: str):
    df = pd.read_csv(csv_path)
    df_reviews = pd.read_csv(csv_reviews_path)
    return df, df_reviews
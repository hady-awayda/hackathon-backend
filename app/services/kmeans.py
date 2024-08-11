from app.ml_models.kmeans import predict_similar_apps
from app.utils.loaders.kmeans_loader import load_datasets

def kmeans_service(user_input_vector: dict):
    df, df_reviews = load_datasets()
    return predict_similar_apps(user_input_vector, df, df_reviews)
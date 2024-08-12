from app.ml_models.kmeans import predict_similar_apps
from app.utils.loaders.loader import load_datasets, load_model

df_cleaned_path = 'database/csv/df_merged_cleaned.csv'
user_reviews_path = 'database/csv/googleplaystore_user_reviews.csv'
kmeans_model_path = 'database/libs/kmeans_with_preprocessor.joblib'

def kmeans_service(user_input_vector: dict, n_similar):
    df, df_reviews = load_datasets(df_cleaned_path, user_reviews_path)
    loaded_model = load_model(kmeans_model_path)
    return predict_similar_apps(user_input_vector, df, df_reviews, loaded_model, n_similar)
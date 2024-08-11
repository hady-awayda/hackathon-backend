from app.utils.loaders.loader import load_datasets, load_model

def load_kmeans_model(user_input_vector: dict, n_similar=5):
    df, df_reviews = load_datasets('csv/df_merged_cleaned.csv', 'csv/googleplaystore_user_reviews.csv')
    loaded_model = load_model('models/kmeans_with_preprocessor.joblib')
    return df, df_reviews, loaded_model
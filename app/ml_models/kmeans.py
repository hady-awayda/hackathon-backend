import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from app.pre_processors.kmeans import preprocess_features

def predict_similar_apps(user_input_vector: dict, df: pd.DataFrame, df_reviews: pd.DataFrame, loaded_model, n_similar):
    X_processed, user_input_vector_processed = preprocess_features(user_input_vector, df, loaded_model)

    similar_indices = find_similar_indices(user_input_vector_processed, X_processed, n_similar)

    detailed_similar_apps, aggregation = aggregate_similar_apps(df, df_reviews, similar_indices)
    
    return detailed_similar_apps, aggregation

def find_similar_indices(user_input_vector_processed, X_processed, n_similar):
    similarities = cosine_similarity(user_input_vector_processed, X_processed).flatten()

    return similarities.argsort()[-(n_similar + 1):-1]

def aggregate_similar_apps(df: pd.DataFrame, df_reviews: pd.DataFrame, similar_indices: np.ndarray[any, any]):
    similar_apps = df.iloc[similar_indices]
    aggregation = similar_apps[['rating', 'reviews', 'size', 'installs', 'price']].agg(['mean', 'std']).to_dict(orient='index')

    detailed_similar_apps = []
    for _, app in similar_apps.iterrows():
        app_name = app['app']
        app_reviews = df_reviews[df_reviews['App'].str.lower() == app_name.lower()]

        reviews_list = [
            {
                'text': review['Translated_Review'],
                'sentiment': review['Sentiment'],
                'sentiment_polarity': review['Sentiment_Polarity'],
                'sentiment_subjectivity': review['Sentiment_Subjectivity']
            }
            for _, review in app_reviews.iterrows()
            if pd.notna(review['Translated_Review']) and pd.notna(review['Sentiment'])
        ]
        
        detailed_similar_apps.append({
            'app': app_name,
            'rating': None if np.isnan(app['rating']) or np.isinf(app['rating']) else app['rating'],
            'reviews': None if np.isnan(app['reviews']) or np.isinf(app['reviews']) else app['reviews'],
            'size': None if np.isnan(app['size']) or np.isinf(app['size']) else app['size'],
            'installs': None if np.isnan(app['installs']) or np.isinf(app['installs']) else app['installs'],
            'price': None if np.isnan(app['price']) or np.isinf(app['price']) else app['price'],
            'all_reviews': reviews_list
        })

    for stat in aggregation:
        for key, value in aggregation[stat].items():
            if np.isnan(value) or np.isinf(value):
                aggregation[stat][key] = None

    return detailed_similar_apps, aggregation
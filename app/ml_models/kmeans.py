import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from app.pre_processors.kmeans import preprocess_features

def predict_similar_apps(user_input_vector: dict, df: pd.DataFrame, df_reviews: pd.DataFrame, loaded_model, n_similar):
    X_processed, user_input_vector_processed = preprocess_features(user_input_vector, df, loaded_model)

    similar_indices = find_similar_indices(user_input_vector_processed, X_processed, n_similar)

    similar_apps, aggregation = aggregate_similar_apps(df, df_reviews, similar_indices)
    
    return similar_apps, aggregation

def find_similar_indices(user_input_vector_processed, X_processed, n_similar):
    similarities = cosine_similarity(user_input_vector_processed, X_processed).flatten()

    return similarities.argsort()[-(n_similar + 1):-1]

def aggregate_similar_apps(df: pd.DataFrame, df_reviews: pd.DataFrame, similar_indices: np.ndarray[any, any]):
    similar_apps = df.iloc[similar_indices]
    aggregation = similar_apps[['rating', 'reviews', 'size', 'installs', 'price']].agg(['mean', 'std'])

    # for key, value in aggregation.items():
    #     aggregation[key] = {k: (None if pd.isna(v) else v) for k, v in value.items()}

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
            'rating': app['rating'],
            'reviews': app['reviews'],
            'size': app['size'],
            'installs': app['installs'],
            'price': app['price'],
            'all_reviews': reviews_list
        })

    # print(detailed_similar_apps, aggregation)
    
    return detailed_similar_apps, aggregation
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from app.utils.loaders.kmeans_loader import load_model

def predict_similar_apps(user_input_vector: dict, df: pd.DataFrame, df_reviews: pd.DataFrame, n_similar=5):
    loaded_model = load_model('models/kmeans_with_preprocessor.joblib')
    preprocessor = loaded_model['preprocessor']
    
    features = ['rating', 'reviews', 'size', 'installs', 'price', 'average_sentiment_analysis', 'average_sentiment_subjectivity']
    
    X = df[features].copy()
    X_processed = preprocessor.transform(X)
    
    user_input_vector_df = pd.DataFrame([user_input_vector], columns=features)
    user_input_vector_processed = preprocessor.transform(user_input_vector_df)
    
    similarities = cosine_similarity(user_input_vector_processed, X_processed).flatten()
    similar_indices = similarities.argsort()[-(n_similar + 1):-1]
    
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
            'rating': app['rating'],
            'reviews': app['reviews'],
            'size': app['size'],
            'installs': app['installs'],
            'price': app['price'],
            'all_reviews': reviews_list
        })
    
    return detailed_similar_apps, aggregation

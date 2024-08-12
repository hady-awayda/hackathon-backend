def find_similar_apps(user_input_vector, n_similar=5):
    import json
    import numpy as np
    import joblib
    import pandas as pd
    from sklearn.metrics.pairwise import cosine_similarity
    from pathlib import Path
    
    model_path = Path('database/libs/kmeans_with_preprocessor.joblib')
    csv_path = Path('database/csv/df_merged_cleaned.csv')
    csv_path_reviews = Path('database/csv/googleplaystore_user_reviews.csv')
    
    loaded_model = joblib.load(model_path)
    preprocessor = loaded_model['preprocessor']
    
    df = pd.read_csv(csv_path)
    df_reviews = pd.read_csv(csv_path_reviews)
    
    features = ['rating', 'reviews', 'size', 'installs', 'price', 'average_sentiment_analysis', 'average_sentiment_subjectivity']
    
    X = df[features].copy()
    X_processed = preprocessor.transform(X)
    
    user_input_vector_df = pd.DataFrame(user_input_vector, columns=features)
    user_input_vector_processed = preprocessor.transform(user_input_vector_df)
    
    app_vector = np.array(user_input_vector_processed).reshape(1, -1)
    
    similarities = cosine_similarity(app_vector, X_processed).flatten()
    similar_indices = similarities.argsort()[-(n_similar + 1):-1]
    
    similar_apps = df.iloc[similar_indices]
    aggregation = similar_apps[['rating', 'reviews', 'size', 'installs', 'price']].agg(['mean', 'std'])
    
    detailed_similar_apps = []

    for _, app in similar_apps.iterrows():
        app_name = app['app']
        
        app_reviews = df_reviews[df_reviews['App'].str.lower() == app_name.lower()]
        
        reviews_list = []
        if not app_reviews.empty:
            for _, review in app_reviews.iterrows():
                if pd.notna(review['Translated_Review']) and pd.notna(review['Sentiment']):
                    reviews_list.append({
                        'text': review['Translated_Review'],
                        'sentiment': review['Sentiment'],
                        'sentiment_polarity': review['Sentiment_Polarity'],
                        'sentiment_subjectivity': review['Sentiment_Subjectivity']
                    })
        detailed_similar_apps.append({
            'app': app_name,
            'rating': app['rating'],
            'reviews': app['reviews'],
            'size': app['size'],
            'installs': app['installs'],
            'price': app['price'],
            'all_reviews': reviews_list
        })
    
    aggregation_json = aggregation.to_dict(orient='index')
    
    return json.dumps({
        'similar_apps': detailed_similar_apps,
        'aggregation': aggregation_json
    })

user_input_vector = [{
    "rating": 4.1,
    "reviews": 190,
    "size": 24,
    "installs": 10500,
    "price": 1.79,
    "average_sentiment_analysis": 0.25,
    "average_sentiment_subjectivity": 0.15
}]

result_json = find_similar_apps(user_input_vector)
print(result_json)

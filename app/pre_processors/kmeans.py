import pandas as pd

def preprocess_features(user_input_vector, df, loaded_model):
    preprocessor = loaded_model['preprocessor']
    features = ['rating', 'reviews', 'size', 'installs', 'price', 'average_sentiment_analysis', 'average_sentiment_subjectivity']

    X_processed = preprocess_X(df, features, preprocessor)
    user_input_vector_processed = preprocess_user_input(user_input_vector, features, preprocessor)

    return X_processed, user_input_vector_processed

def preprocess_X(df, features, preprocessor):
    X = df[features].copy()
    
    return preprocessor.transform(X)

def preprocess_user_input(user_input_vector, features, preprocessor):
    user_input_vector_df = pd.DataFrame([user_input_vector], columns=features)

    return preprocessor.transform(user_input_vector_df)
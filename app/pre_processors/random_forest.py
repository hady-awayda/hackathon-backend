import pandas as pd

def prepare_input_data(input_series: dict) -> pd.DataFrame:
    input_series_renamed = {
        "category": str(input_series["category"]),
        "size": int(input_series["size"]),
        "type": str(input_series["type"]),
        "price": float(input_series["price"]),
        "content rating": str(input_series["content_rating"]),
        "genres": str(input_series["genres"]),
        "current ver": str(input_series["current_ver"]),
        "android ver": str(input_series["android_ver"]),
        "sentiment": int(input_series["sentiment"]),
    }

    test_data = pd.DataFrame([input_series_renamed])
    return test_data
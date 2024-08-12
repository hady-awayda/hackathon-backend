from fastapi import HTTPException
import numpy as np
import pandas as pd
from app.schemas.kmeans import KmeansRequest
from app.services.kmeans import kmeans_service

def post_process_response(data):
    if isinstance(data, dict):
        return {k: post_process_response(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [post_process_response(v) for v in data]
    elif isinstance(data, pd.DataFrame):
        return data.where(pd.notnull(data), None).to_dict(orient='records')
    elif isinstance(data, pd.Series):
        return data.where(pd.notnull(data), None).to_dict()
    elif pd.isna(data) or isinstance(data, float) and np.isnan(data):
        return None
    return data

def kmeans_controller(request: KmeansRequest, n: int):
    try:
        input_series = request.model_dump()
        similar_apps, aggregation = kmeans_service(input_series, n)
        processed_response = post_process_response({'similar_apps': similar_apps, 'aggregation': aggregation})
        return processed_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
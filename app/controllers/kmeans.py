from fastapi import HTTPException
from app.schemas.kmeans import KmeansRequest
from app.services.kmeans import kmeans_service

def kmeans_controller(request: KmeansRequest):
    try:
        input_series = request.model_dump()
        similar_apps, aggregation = kmeans_service(input_series)
        return {'similar_apps': similar_apps, 'aggregation': aggregation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
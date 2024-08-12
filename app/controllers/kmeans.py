from fastapi import HTTPException
from app.schemas.kmeans import KmeansRequest
from app.services.kmeans import kmeans_service

def kmeans_controller(request: KmeansRequest, n: int):
    try:
        if n > 20:
            raise HTTPException(status_code=400, detail="n must be less than 20")
        
        input_series = request.model_dump()
        detailed_similar_apps, aggregation_json = kmeans_service(input_series, n)
        
        return {
            'similar_apps': detailed_similar_apps,
            'aggregation': aggregation_json
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
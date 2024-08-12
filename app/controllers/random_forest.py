from fastapi import HTTPException
from app.schemas.random_forest import RandomForestRequest
from app.services.random_forest import random_forest_service

def random_forest_controller(request: RandomForestRequest):
    try:
        input_series = request.model_dump()
        prediction = random_forest_service(input_series)
        
        return {
            "prediction": prediction
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
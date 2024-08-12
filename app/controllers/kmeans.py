import json
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import numpy as np
from app.schemas.kmeans import KmeansRequest
from app.services.kmeans import kmeans_service

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, float) and np.isnan(obj):
            return None
        return super().default(obj)
    
def kmeans_controller(request: KmeansRequest, n: int):
    try:
        input_series = request.model_dump()
        res = kmeans_service(input_series, n)
        return JSONResponse(content=json.loads(json.dumps(res, cls=CustomJSONEncoder)))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
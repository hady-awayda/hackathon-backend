from fastapi import APIRouter, Depends
from app.controllers.predict_controller import predict_controller
from app.middleware.checkFreeUser import check_free_user
from app.middleware.checkPaidUser import check_paid_user
from app.schemas.predict_model import PredictRequest

router = APIRouter()

@router.post("/predict/random_forest_classifier")
def predict_random_forest_route(
    request: PredictRequest, 
    current_user: dict = Depends(check_free_user)
):
    return predict_controller(request)

@router.post("/predict/clustering_classifier")
def predict_clustering_route(
    request: PredictRequest, 
    current_user: dict = Depends(check_paid_user)
):
    return predict_controller(request)
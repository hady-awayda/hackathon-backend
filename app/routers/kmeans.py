from fastapi import APIRouter, Depends, Query
from app.controllers.kmeans import kmeans_controller
from app.middleware.checkPaidUser import check_paid_user
from app.schemas.kmeans import KmeansRequest

router = APIRouter()

@router.post("/kmeans_classifier")
def kmeans_route(
    request: KmeansRequest, 
    n: int = Query(5),
    current_user: dict = Depends(check_paid_user)
):
    return kmeans_controller(request, n)
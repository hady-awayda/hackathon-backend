from fastapi import APIRouter, Depends
from app.controllers.random_forest import random_forest_controller
from app.middleware.checkFreeUser import check_free_user
from app.schemas.random_forest import RandomForestRequest

router = APIRouter()

@router.post("/random_forest_classifier")
def random_forest_route(
    request: RandomForestRequest, 
    current_user: dict = Depends(check_free_user)
):
    return random_forest_controller(request)
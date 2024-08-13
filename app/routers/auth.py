from fastapi import APIRouter, Response, status
from app.controllers.auth import register_controller, login_controller
from app.schemas.auth import RegisterRequest, LoginRequest

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_route(request: RegisterRequest, response: Response):
    return register_controller(request, response)

@router.post("/login", status_code=status.HTTP_200_OK)
def login_route(request: LoginRequest, response: Response):
    return login_controller(request, response)
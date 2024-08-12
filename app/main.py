from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.auth import router as auth_router
from app.routers.kmeans import router as kmeans_router
from app.routers.random_forest import router as random_forest_router
from app.routers.user_ideas import router as user_ideas_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/v1/auth")
app.include_router(user_ideas_router, prefix="/api/v1/user_ideas")
app.include_router(kmeans_router, prefix="/api/v1/predict")
app.include_router(random_forest_router, prefix="/api/v1/predict")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
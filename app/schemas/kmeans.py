from pydantic import BaseModel

class KmeansRequest(BaseModel):
    rating: float
    reviews: int
    size: int
    installs: int
    price: float
    average_sentiment_analysis: float
    average_sentiment_subjectivity: float

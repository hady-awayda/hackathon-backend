from sqlalchemy import func
from sqlalchemy.orm import Session
from config.database import get_db
from app.models.user_prediction import UserPrediction

db: Session = next(get_db())

def get_prediction_by_id(prediction_id: int):
	return db.query(UserPrediction).filter(UserPrediction.id == prediction_id, UserPrediction.deletedAt == None).first()

def create_prediction(prediction: UserPrediction):
	try:
		db.add(prediction)
		db.commit()
		return "Prediction created successfully"
	except Exception as e:
		db.rollback()
		raise e

def update_prediction():
	try:
		db.commit()
		return "Prediction updated successfully"
	except Exception as e:
		db.rollback()
		raise e

def delete_prediction(prediction: UserPrediction):
	try:
		prediction.deletedAt = func.now()
		db.commit()
		return "Prediction deleted successfully"
	except Exception as e:
		db.rollback()
		raise e
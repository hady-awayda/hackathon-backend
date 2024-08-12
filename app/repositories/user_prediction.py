from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.user_prediction import UserPrediction

def get_prediction_by_id(db: Session, prediction_id: int):
    return db.query(UserPrediction).filter(UserPrediction.id == prediction_id, UserPrediction.deleted_at == None).first()

def create_prediction(db: Session, prediction: UserPrediction):
	try:
		db.add(prediction)
		db.commit()
		db.refresh(prediction)
		return prediction
	except Exception as e:
		db.rollback()
		raise e

def update_prediction(db: Session, prediction: UserPrediction):
    try:
        db.add(prediction)
        db.commit()
        db.refresh(prediction)
        return prediction
    except Exception as e:
        db.rollback()
        raise e

def delete_prediction(db: Session, prediction: UserPrediction):
    try:
        prediction.deletedAt = func.now()
        db.commit()
        return prediction
    except Exception as e:
        db.rollback()
        raise e
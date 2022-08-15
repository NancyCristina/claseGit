from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return (
        db.query(models.Mock_Data)
        .filter(models.Mock_Data.id == user_id)
        .first()
        .__dict__
    )

def get_user_by_id(db: Session, user_id: int):
    return (
        db.query(models.Mock_Data)
        .filter(models.Mock_Data.id == user_id)
        .first()
    )

def get_all_users(db: Session):
    return db.query(models.Mock_Data).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.Mock_Data(
        id =user.id ,
        email=user.email, 
        first_name= user.first_name,
        last_name= user.last_name,
        gender = user.gender,
        ip_address =user.ip_address,
        city = user.city,
        guid = user.guid
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.__dict__
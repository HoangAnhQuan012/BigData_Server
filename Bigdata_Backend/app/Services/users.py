from sqlalchemy.orm import Session
from Models.models import User
from Schemas.schemas import Userschema
from utilis import hash

def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: Userschema):
    print(user)
    _user = User(username=user.username, password= hash(user.password), permission = user.permission, email = user.email, phone = user.phone)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


def remove_user(db: Session, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()


def update_user(db: Session, user_id: int, username: str, password: str, permission: int):
    _user = get_user_by_id(db=db, user_id=user_id)

    _user.username = username 
    _user.password = password
    _user.permission = permission

    db.commit()
    db.refresh(_user)
    return _user

from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from Schemas.schemas import Userschema, Response
from connect_db import get_db 

import Services.users as crud

router = APIRouter()

@router.post("/create")
async def create_user_service(request: Userschema, db: Session = Depends(get_db)):
    try:
        user = crud.create_user(db, user=request)
        return Response(code=200,status='Success',message='Ok',result=user.id)
    except Exception as e:
        raise

@router.get("/")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        _users = crud.get_user(db, skip, limit)
        return Response(status="Ok", code="200", message="Success fetch all data", result=_users)
    except Exception as e:
        raise

@router.put("/update/{id}")
async def update_user(id:int,request: Userschema, db: Session = Depends(get_db)):
    try:
        _user = crud.update_user(db, user_id=id,
                             username=request.username, password=request.password, permission = request.permission)
        return Response(status="Ok", code="200", message="Success update data", result=_user.id)
    except Exception as e:
        raise

@router.delete("/delete/{id}")
async def delete_user(id: int,request: Userschema,  db: Session = Depends(get_db)):
    try:
        crud.remove_user(db, user_id= id)
        return Response(status="Ok", code="200", message="Success delete data",result=id)
    except Exception as e:
        raise

from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from Schemas.schemas import RankedPrescSchema, Response
from connect_db import get_db 

import Services.presc_of_the_city as crud

router = APIRouter()

@router.get("/visualize/presc_per_populations")
async def show_presc_per_populations( db: Session = Depends(get_db)):
    try:
        quantitle_list = crud.get_presc_per_populations(db)
        return Response(code=200,status='Success',message='Ok',result=quantitle_list)
    except Exception as e:
        print(str(e))
        raise
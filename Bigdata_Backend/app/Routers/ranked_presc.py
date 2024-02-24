from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from Schemas.schemas import RankedPrescSchema, Response
from connect_db import get_db 

import Services.ranked_presc as crud

router = APIRouter()

@router.post("/create")
async def create_ranked_presc_service(request: RankedPrescSchema, db: Session = Depends(get_db)):
    try:
        ranked_presc = crud.create_ranked_presc(db, ranked_presc=request)
        return Response(code=200,status='Success',message='Ok',result=ranked_presc.presc_id)
    except Exception as e:
        raise

@router.get("/")
async def get_ranked_prescs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        _ranked_prescs = crud.get_ranked_presc(db, skip, limit)
        return Response(status="Ok", code="200", message="Success fetch all data", result=_ranked_prescs)
    except Exception as e:
         return Response(status="Error", code="500", message="Reject fetch data", result='')


@router.put("/update/{id}")
async def update_ranked_presc(id:int,request: RankedPrescSchema, db: Session = Depends(get_db)):
    try:
        _ranked_presc = crud.update_ranked_presc(db, presc_id=id,
                        presc_fullname=request.presc_fullname, presc_state=request.presc_state,Country_name=request.Country_name,years_of_exp=request.years_of_exp,tx_cnt=request.tx_cnt,total_day_supply=request.total_day_supply, total_drug_cost=request.total_drug_cost, dense_rank=request.dense_rank)
        return Response(status="Ok", code="200", message="Success update data", result=_ranked_presc.presc_id)
    except Exception as e:
         print(str(e))
         raise
         return Response(status="Error", code="500", message="Reject update data", result='')


@router.delete("/delete/{id}")
async def delete_ranked_presc(id: int,request: RankedPrescSchema,  db: Session = Depends(get_db)):
    try:
        crud.remove_ranked_presc(db, presc_id= id)
        return Response(status="Ok", code="200", message="Success delete data",result=id)
    except Exception as e:
        return Response(status="Error", code="500", message="Reject delete data", result='')


@router.get("/visualize/rank")
async def get_rank_num(db: Session = Depends(get_db)):
    try:
        result_list = crud.coung_by_rank(db)
        return Response(status="Ok", code="200", message="Success delete data",result=result_list)
    except Exception as e:
        return Response(status="Error", code="500", message="Reject delete data", result='')

@router.get("/visualize/percentage_yoe")
async def get_percentage_yoe(db: Session = Depends(get_db)):
    try:
        result_list = crud.calc_percentage_yoe(db)
        return Response(status="Ok", code="200", message="Success delete data",result=result_list)
    except Exception as e:
        print(str(e))
        return Response(status="Error", code="500", message="Reject delete data", result='')
    



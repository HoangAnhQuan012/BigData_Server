from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from Schemas.schemas import DfPrescSelSchema, Response, DfPrescUpdateSelSchema
from connect_db import get_db
from typing import Optional

import Services.df_presc_sel as crud

router = APIRouter()

@router.post("/create")
async def create_df_presc_sel_service(request: DfPrescSelSchema, db: Session = Depends(get_db)):
    try:
        df_presc_sel = crud.create_df_presc_sel(db, df_presc_sel=request)
        return Response(code=200,status='Success',message='Ok',result=df_presc_sel.presc_id)
    except Exception as e:
        raise

@router.get("/")
async def get_df_presc_sels(keyword: Optional[str] = '', skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        _df_presc_sels = crud.get_df_presc_sel(db, keyword, skip, limit)
        return Response(status="Ok", code="200", message="Success fetch all data", result=_df_presc_sels)
    except Exception as e:
        print(str(e))
        return Response(status="Error", code="500", message="Reject fetch data", result='')
    
@router.put("/update/{presc_id}")
async def update_df_presc_sel(presc_id: str, request: DfPrescUpdateSelSchema, db: Session = Depends(get_db)):
    try:
        _df_presc_sel = crud.update_df_presc_sel(db, presc_id=presc_id, presc_city=request.presc_city, presc_state=request.presc_state, presc_spclty=request.presc_spclty, drug_name=request.drug_name, tx_cnt=request.tx_cnt, total_day_supply=request.total_day_supply, total_drug_cost=request.total_drug_cost, years_of_exp=request.years_of_exp, Country_name=request.Country_name, presc_fullname=request.presc_fullname)
        return Response(status="Ok", code="200", message="Success update data", result=_df_presc_sel)
    except Exception as e:
        print(str(e))
        raise

@router.delete("/delete/{presc_id}")
async def delete_df_presc_sel(presc_id: str, db: Session = Depends(get_db)):
    try:
        crud.remove_df_presc_sel(db, presc_id=presc_id)
        return Response(status="Ok", code="200", message="Success delete data",result=presc_id)
    except Exception as e:
        return Response(status="Error", code="500", message="Reject delete data", result='')

@router.get("/{presc_id}")
async def get_df_presc_sel_by_id(presc_id: str, db: Session = Depends(get_db)):
    try:
        _df_presc_sel = crud.get_df_presc_sel_by_id(db, presc_id=presc_id)
        return Response(status="Ok", code="200", message="Success fetch data", result=_df_presc_sel)
    except Exception as e:
        return Response(status="Error", code="500", message="Reject fetch data", result='')
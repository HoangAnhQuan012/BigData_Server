from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from Schemas.schemas import DfCitySelSchema, Response, DfCitySelUpdateSchemaDto
from connect_db import get_db
from typing import Optional

import Services.df_city_sel as crud

router = APIRouter()

@router.post("/create")
async def create_df_city_sel_service(request: DfCitySelSchema, db: Session = Depends(get_db)):
    try:
        df_city_sel = crud.create_df_city_sel(db, df_city_sel=request)
        return Response(code=200,status='Success',message='Ok',result=df_city_sel.city)
    except Exception as e:
        raise

@router.get("/")
async def get_df_city_sels(keyword: Optional[str] = '', skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        _df_city_sels = crud.get_df_city_sel(db, keyword, skip, limit)
        return Response(status="Ok", code="200", message="Success fetch all data", result=_df_city_sels)
    except Exception as e:
        print(str(e))
        return Response(status="Error", code="500", message="Reject fetch data", result='')
    
@router.put("/update/{city}/{state_id}")
async def update_df_city_sel(city: str, state_id: str, request: DfCitySelUpdateSchemaDto, db: Session = Depends(get_db)):
    try:
        _df_city_sel = crud.update_df_city_sel(db, city=city, state_id=state_id, state_name=request.state_name, country_name=request.country_name, population=request.population, zips=request.zips)
        return Response(status="Ok", code="200", message="Success update data", result=_df_city_sel)
    except Exception as e:
        print(str(e))
        raise

@router.delete("/delete/{city}/{state_id}")
async def delete_df_city_sel(city: str, state_id: str, db: Session = Depends(get_db)):
    try:
        crud.remove_df_city_sel(db, city=city, state_id=state_id)
        return Response(status="Ok", code="200", message="Success delete data",result=city + state_id)
    except Exception as e:
        return Response(status="Error", code="500", message="Reject delete data", result='')
    
@router.get("/{city}/{state_id}")
async def get_df_city_sel_by_id(city: str, state_id: str, db: Session = Depends(get_db)):
    try:
        _df_city_sel = crud.get_df_city_sel_by_id(db, city=city, state_id=state_id)
        return Response(status="Ok", code="200", message="Success fetch data", result=_df_city_sel)
    except Exception as e:
        return Response(status="Error", code="500", message="Reject fetch data", result='')
    

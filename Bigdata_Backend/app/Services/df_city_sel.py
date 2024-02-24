from sqlalchemy import String
from sqlalchemy.orm import Session
from Models.models import DfCitySel
from Schemas.schemas import DfCitySelSchema
from typing import Optional
from sqlalchemy import desc, asc

def get_df_city_sel(db: Session, keyword: Optional[str] = '', skip: int = 0, limit: int = 100):
    query = db.query(DfCitySel).filter(DfCitySel.city.contains(keyword))
    records = query.order_by(asc(DfCitySel.city)).offset(skip).limit(limit).all()
    total_count = query.count()
    page_Result = {
        "Items": records,
        "Total_count": total_count
    }
    return page_Result

def get_df_city_sel_by_id(db: Session, city: str, state_id: str):
    return db.query(DfCitySel).filter(DfCitySel.city == city, DfCitySel.state_id == state_id).first()

def create_df_city_sel(db: Session, df_city_sel: DfCitySelSchema):
    _df_city_sel_schema = DfCitySel(
        city = df_city_sel.city,
        state_id = df_city_sel.state_id,
        state_name = df_city_sel.state_name,
        county_name = df_city_sel.country_name,
        population = df_city_sel.population,
        zips = df_city_sel.zips,
        )
    db.add(_df_city_sel_schema)
    db.commit()
    db.refresh(_df_city_sel_schema)
    return _df_city_sel_schema

def remove_df_city_sel(db: Session, city: str, state_id: str):
    _df_city_sel_schema = get_df_city_sel_by_id(db=db, city=city, state_id=state_id)
    db.delete(_df_city_sel_schema)
    db.commit()

def update_df_city_sel(db: Session, city: str, state_id: str, state_name: str, country_name: str, population:int, zips:str):
    _df_city_sel_schema = get_df_city_sel_by_id(db=db, city=city, state_id=state_id)

    _df_city_sel_schema.state_name = state_name
    _df_city_sel_schema.county_name = country_name
    _df_city_sel_schema.population = population
    _df_city_sel_schema.zips = zips

    db.commit()
    db.refresh(_df_city_sel_schema)
    return _df_city_sel_schema
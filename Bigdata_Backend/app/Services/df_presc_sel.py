from sqlalchemy import String
from sqlalchemy.orm import Session
from Models.models import DfPrescSel
from Schemas.schemas import DfPrescSelSchema
from sqlalchemy import desc, asc
from typing import Optional

def get_df_presc_sel(db: Session, keyword: Optional[str] = '', skip: int = 0, limit: int = 100):
    query = db.query(DfPrescSel).filter(DfPrescSel.presc_fullname.contains(keyword))
    records = query.order_by(asc(DfPrescSel.Country_name)).offset(skip).limit(limit).all()
    total_count = query.count()
    page_Result = {
        "Items": records,
        "Total_count": total_count
    }
    return page_Result

def get_df_presc_sel_by_id(db: Session, presc_id: str):
    return db.query(DfPrescSel).filter(DfPrescSel.presc_id == presc_id).first()

def create_df_presc_sel(db: Session, df_presc_sel: DfPrescSelSchema):
    _df_presc_sel_schema = DfPrescSel(
        presc_id = df_presc_sel.presc_id,
        presc_city = df_presc_sel.presc_city,
        presc_state = df_presc_sel.presc_state,
        presc_spclt = df_presc_sel.presc_spclt,
        drug_name = df_presc_sel.drug_name,
        tx_cnt = df_presc_sel.tx_cnt,
        total_day_supply = df_presc_sel.total_day_supply,
        total_drug_cost = df_presc_sel.total_drug_cost,
        years_of_exp = df_presc_sel.years_of_exp,
        Country_name = df_presc_sel.Country_name,
        presc_fullname = df_presc_sel.presc_fullname,
        )
    db.add(_df_presc_sel_schema)
    db.commit()
    db.refresh(_df_presc_sel_schema)
    return _df_presc_sel_schema

def remove_df_presc_sel(db: Session, presc_id: str):
    _df_presc_sel_schema = get_df_presc_sel_by_id(db=db, presc_id=presc_id)
    db.delete(_df_presc_sel_schema)
    db.commit()

def update_df_presc_sel(db: Session, presc_id: str, presc_city: str, presc_state: str, presc_spclty: str, drug_name: str, tx_cnt: int, total_day_supply: int, total_drug_cost: float, years_of_exp: int, Country_name: str, presc_fullname: str):
    _df_presc_sel_schema = get_df_presc_sel_by_id(db=db, presc_id=presc_id)

    _df_presc_sel_schema.presc_city = presc_city
    _df_presc_sel_schema.presc_state = presc_state
    _df_presc_sel_schema.presc_spclty = presc_spclty
    _df_presc_sel_schema.drug_name = drug_name
    _df_presc_sel_schema.tx_cnt = tx_cnt
    _df_presc_sel_schema.total_day_supply = total_day_supply
    _df_presc_sel_schema.total_drug_cost = total_drug_cost
    _df_presc_sel_schema.years_of_exp = years_of_exp
    _df_presc_sel_schema.Country_name = Country_name
    _df_presc_sel_schema.presc_fullname = presc_fullname

    db.commit()
    db.refresh(_df_presc_sel_schema)
    return _df_presc_sel_schema

from sqlalchemy import String
from sqlalchemy.orm import Session
from Models.models import RankedPresc
from Schemas.schemas import RankedPrescSchema
from utilis import hash
from sqlalchemy import and_

def get_ranked_presc(db: Session, skip: int = 0, limit: int = 100):
    return db.query(RankedPresc).offset(skip).limit(limit).all()


def get_ranked_by_id(db: Session, presc_id: int):
    return db.query(RankedPresc).filter(RankedPresc.presc_id.cast(String) == str(presc_id)).first()


def create_ranked_presc(db: Session, ranked_presc: RankedPrescSchema):
    _ranked_schema = RankedPresc(
        presc_id = ranked_presc.presc_id,
        presc_fullname = ranked_presc.presc_fullname,
        presc_state = ranked_presc.presc_state,
        Country_name = ranked_presc.Country_name,
        years_of_exp = ranked_presc.years_of_exp,
        tx_cnt = ranked_presc.tx_cnt,
        total_day_supply = ranked_presc.total_day_supply,
        total_drug_cost = ranked_presc.total_drug_cost,
        dense_rank = ranked_presc.dense_rank,
        )
    db.add(_ranked_schema)
    db.commit()
    db.refresh(_ranked_schema)
    return _ranked_schema


def remove_ranked_presc(db: Session, presc_id: int):
    _ranked_schema = get_ranked_by_id(db=db, presc_id=presc_id)
    db.delete(_ranked_schema)
    db.commit()


def update_ranked_presc(db: Session, presc_id: int, presc_fullname: str, presc_state: str, Country_name: str, years_of_exp:int, tx_cnt:int, total_day_supply:int, total_drug_cost:float, dense_rank:int):
    _ranked_schema = get_ranked_by_id(db=db, presc_id=presc_id)

    _ranked_schema.presc_fullname = presc_fullname 
    _ranked_schema.presc_state = presc_state
    _ranked_schema.Country_name = Country_name
    _ranked_schema.year_of_exp = years_of_exp
    _ranked_schema.tx_cnt = tx_cnt
    _ranked_schema.total_day_supply = total_day_supply
    _ranked_schema.total_drug_cost = total_drug_cost
    _ranked_schema.dense_rank = dense_rank

    db.commit()
    db.refresh(_ranked_schema)
    return _ranked_schema


def coung_by_rank(db: Session):
    result_list = []
    num_one = db.query(RankedPresc).filter(RankedPresc.dense_rank == 1).count()
    num_two = db.query(RankedPresc).filter(RankedPresc.dense_rank == 2).count()
    num_three = db.query(RankedPresc).filter(RankedPresc.dense_rank == 3).count()
    num_four = db.query(RankedPresc).filter(RankedPresc.dense_rank == 4).count()
    num_five = db.query(RankedPresc).filter(RankedPresc.dense_rank == 5).count()
    result_list.append(num_one)
    result_list.append(num_two)
    result_list.append(num_three)
    result_list.append(num_four)
    result_list.append(num_five)
    return result_list

def calc_percentage_yoe(db: Session):
    result_list = []
    range1 = db.query(RankedPresc.years_of_exp).filter(and_(RankedPresc.years_of_exp >= 20, RankedPresc.years_of_exp<=30)).count()
    range2 = db.query(RankedPresc.years_of_exp).filter(and_(RankedPresc.years_of_exp >= 30, RankedPresc.years_of_exp<=40)).count()
    range3 = db.query(RankedPresc.years_of_exp).filter(and_(RankedPresc.years_of_exp >= 40, RankedPresc.years_of_exp<=50)).count()
    result_list.append(range1)
    result_list.append(range2)
    result_list.append(range3)
    return result_list



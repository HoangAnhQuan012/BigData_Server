
from sqlalchemy import String
from sqlalchemy.orm import Session
from Models.models import PrescCity
from utilis import hash

def get_presc_per_populations(db: Session):
    presc_cities = db.query(PrescCity).filter(PrescCity.population > 0, PrescCity.presc_counts > 0).all()
    temp_list = [int(city.presc_counts)/int(city.population) for city in presc_cities]
    quantile1 = len([i for i in temp_list if i < 0.0125 and i > 0.0])
    quantile2 = len([i for i in temp_list if i <0.025 and i > 0.0125])
    quantile3 = len([i for i in temp_list if i < 0.0375 and i > 0.025])
    quantile4 = len([i for i in temp_list if i > 0.0375])
    return [quantile1,quantile2,quantile3,quantile4 ]




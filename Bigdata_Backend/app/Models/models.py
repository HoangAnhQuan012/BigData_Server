from sqlalchemy import  Column, Integer, String, Text, BigInteger
from config import Base

class User(Base):
    __tablename__ ="users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    permission = Column(Integer, nullable=False)

class RankedPresc(Base):
    __tablename__="ranked_presc"

    presc_id = Column(String, primary_key=True, unique=True)
    presc_fullname = Column(String, nullable=False)
    presc_state = Column(String, nullable=False)
    Country_name = Column(String, nullable=False)
    years_of_exp = Column(Integer, nullable=False)
    tx_cnt = Column(Integer, nullable=False)
    total_day_supply = Column(Integer, nullable=False)
    total_drug_cost = Column(Integer, nullable=False)
    dense_rank = Column(Integer, nullable=False)

class DfCitySel(Base):
    __tablename__="df_city_sel"

    city = Column(String, primary_key=True)
    state_id = Column(String, primary_key=True, nullable=False)
    state_name = Column(String, nullable=False)
    county_name = Column(String, nullable=False)
    population = Column(Integer, nullable=False)
    zips = Column(String, nullable=False)

class DfPrescSel(Base):
    __tablename__="df_presc_sel"

    presc_id = Column(String, primary_key=True)
    presc_city = Column(String, nullable=False)
    presc_state = Column(String, nullable=False)
    presc_spclt = Column(String, nullable=False)
    drug_name = Column(String, nullable=False)
    tx_cnt = Column(Integer, nullable=False)
    total_day_supply = Column(Integer, nullable=False)
    total_drug_cost = Column(Integer, nullable=False)
    years_of_exp = Column(Integer, nullable=False)
    Country_name = Column(String, nullable=False)
    presc_fullname = Column(String, nullable=False)

class PrescCity(Base):
    __tablename__="presc_of_the_city"

    city = Column(String, primary_key=True)
    state_name = Column(String, primary_key=True, nullable=False)
    county_name = Column(String, nullable=False, primary_key=True)
    population = Column(Integer, nullable=False)
    zipcounts = Column(Integer, nullable=False)
    presc_counts = Column(BigInteger, nullable=False)
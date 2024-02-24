from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class Userschema(BaseModel):
    username: str
    password: str
    permission: int
    email: Optional[str]
    phone: Optional[str]

    class Config:
        orm_mode = True

class RankedPrescSchema(BaseModel):
    presc_id: str
    presc_fullname: str
    presc_state: str
    Country_name: str
    years_of_exp: int
    tx_cnt: int
    total_day_supply: int
    total_drug_cost: float
    dense_rank: int 


    class Config:
        orm_mode = True

class DfCitySelSchema(BaseModel):
    city: str
    state_id: str
    state_name: str
    country_name: str
    population: int
    zips: str
    class Config:
        orm_mode = True

class DfCitySelUpdateSchemaDto(BaseModel):
    state_name: str
    country_name: str
    population: int
    zips: str
    class Config:
        orm_mode = True

class DfPrescSelSchema(BaseModel):
    presc_id: str
    presc_city: str
    presc_state: str
    presc_spclt: str
    drug_name: str
    tx_cnt: int
    total_day_supply: int
    total_drug_cost: float
    years_of_exp: int
    Country_name: str
    presc_fullname: str
    class Config:
        orm_mode = True

class DfPrescUpdateSelSchema (BaseModel):
    presc_city: str
    presc_state: str
    presc_spclty: str
    drug_name: str
    tx_cnt: int
    total_day_supply: int
    total_drug_cost: float
    years_of_exp: int
    Country_name: str
    presc_fullname: str
    class Config:
        orm_mode = True


# class Request(GenericModel, Generic[T]):
#     parameter: Optional[T] = Field(...)


# class RequestUser(BaseModel):
#     print(Field(...))
#     parameter: Userschema = Field(...)


class Response():
    code: str
    status: str
    message: str
    result: str 
    def __init__(self,code, status, message, result):    
        self.code = code
        self.status = status
        self.message = message
        self.result = result

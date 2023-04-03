from typing import List
from pydantic import BaseModel

class MtrCountrySchema(BaseModel):
    is_active:bool
    country_id:int
    country_code:str
    country_name:str
    country_language:str
    country_phone:str
    currency_id:int

    class Config:
        orm_mode = True

class MtrCountryResponse(BaseModel):
    status:str
    msg_status:str
    data:List[MtrCountrySchema]
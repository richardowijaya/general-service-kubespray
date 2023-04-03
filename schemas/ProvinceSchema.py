from typing import List
from pydantic import BaseModel

class MtrProvinceSchema(BaseModel):
    is_active:bool
    province_id:int
    province_code:str
    province_name:str
    country_id:int

    class Config:
        orm_mode = True

class MtrProvinceResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrProvinceSchema]

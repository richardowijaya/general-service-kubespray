from typing import List, Optional
from pydantic import BaseModel

class MtrAftersalesAreaSchema(BaseModel):
    is_active:bool
    aftersales_area_id:int
    aftersales_area_code:str
    aftersales_area_name:str

    class Config:
        orm_mode = True

class MtrAftersalesAreaResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrAftersalesAreaSchema]

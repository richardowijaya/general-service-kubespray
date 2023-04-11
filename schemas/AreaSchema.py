from typing import List
from pydantic import BaseModel

class MtrAreaSchema(BaseModel):
    is_active:bool
    area_id:int
    area_code:str
    description:str
    region_id:int #relation with user in login module/service

    class Config:
        orm_mode_= True

class MtrAreaRequest(BaseModel):
    area_code:str
    description:str
    region_id:int

class MtrAreaResponses(BaseModel):
    status_code:int
    msg_status:str
    data:List[MtrAreaSchema]

class MtrAreaResponse(BaseModel):
    status_code:int
    msg_status:str
    data:MtrAreaSchema
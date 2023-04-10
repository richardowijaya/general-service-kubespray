from typing import List
from pydantic import BaseModel

class MtrAreaSchema(BaseModel):
    is_active:bool
    area_id:int
    area_code:str
    description:str
    user_id:int #relation with user in login module/service

    class Config:
        orm_mode_= True

class MtrAreaResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrAreaSchema] 
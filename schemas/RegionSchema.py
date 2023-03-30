from typing import List
from pydantic import BaseModel

class MtrRegionSchema(BaseModel):
    is_active:bool
    regional_id:int
    regional_code:str
    regional_name:str
    user_id:int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
class MtrRegionResponse(BaseModel):
    status:str
    msg_status:str
    data:List[MtrRegionSchema]
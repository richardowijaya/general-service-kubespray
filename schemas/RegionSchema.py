from typing import List, Optional
from pydantic import BaseModel,Field

class MtrRegionSchema(BaseModel):
    is_active:Optional[bool]=None
    regional_id:Optional[int]=None
    regional_code:str
    regional_name:str
    user_id:int

    class Config:
        orm_mode = True

class MtrRegionRequest(BaseModel):
    regional_code:str
    regional_name:str
    user_id:int

class MtrRegionResponses(BaseModel):
    status_code:int
    msg_status:str
    data:List[MtrRegionSchema]

class MtrRegionResponse(BaseModel):
    status_code:int
    msg_status:str
    data:MtrRegionSchema
<<<<<<< HEAD
from typing import List, Optional
from pydantic import BaseModel

class MtrRegionSchema(BaseModel):
    is_active:Optional[bool]=None
    region_id:Optional[int]=None
    region_code:str
    region_name:str
    user_id:int

    class Config:
        orm_mode = True

class MtrRegionRequest(BaseModel):
    region_code:str
    region_name:str
    user_id:int

class MtrRegionResponses(BaseModel):
    status_code:int
    msg_status:str
    data:List[MtrRegionSchema]

class MtrRegionResponse(BaseModel):
    status_code:int
    msg_status:str
=======
from typing import List, Optional
from pydantic import BaseModel

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
>>>>>>> 6c332901c44706e2cd630677bcf753c81a5cd6b3
    data:MtrRegionSchema
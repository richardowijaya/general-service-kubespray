from typing import List, Optional
from pydantic import BaseModel


class MtrAreaSchema(BaseModel):
    is_active:Optional[bool]=None
    area_id:Optional[int]=None
    area_code:str
    description:str
<<<<<<< HEAD
    region_id:int
=======
    regional_id:int
>>>>>>> 6c332901c44706e2cd630677bcf753c81a5cd6b3

    class Config:
        orm_mode = True

class MtrAreaRequest(BaseModel):
    area_code:str
    description:str
<<<<<<< HEAD
    region_id:int
=======
    regional_id:int
>>>>>>> 6c332901c44706e2cd630677bcf753c81a5cd6b3

class MtrAreaResponses(BaseModel):
    status_code:int
    msg_status:str
    data:List[MtrAreaSchema]

class MtrAreaResponse(BaseModel):
    status_code:int
    msg_status:str
    data:MtrAreaSchema

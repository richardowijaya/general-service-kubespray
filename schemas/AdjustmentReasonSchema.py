from typing import List, Optional
from pydantic import BaseModel

class MtrAdjustmentReasonGetSchema(BaseModel):
    adjustment_reason_code:Optional[str] = None
    adjustment_reason_name:Optional[str] = None
    
    class Config:
        orm_mode = True

class MtrAdjustmentReasonResponses(BaseModel):
    status_code : int
    message : str
    data : List[MtrAdjustmentReasonGetSchema]

class MtrAdjustmentReasonResponse(BaseModel):
    status_code : int
    message : str
    data : MtrAdjustmentReasonGetSchema
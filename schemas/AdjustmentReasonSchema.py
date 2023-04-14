from typing import List, Optional
from pydantic import BaseModel

class MtrAdjustmentReasonGetSchema(BaseModel):
    adjustment_reason_code:Optional[str] = None
    adjustment_reason_name:Optional[str] = None
    
    class Config:
<<<<<<< HEAD
        orm_mode = True

class MtrAdjustmentReasonResponses(BaseModel):
    status_code : int
    message : str
    data : List[MtrAdjustmentReasonGetSchema]

class MtrAdjustmentReasonResponse(BaseModel):
    status_code : int
    message : str
    data : MtrAdjustmentReasonGetSchema
=======
        orm_mode = True
>>>>>>> 6c332901c44706e2cd630677bcf753c81a5cd6b3

from typing import List, Optional
from pydantic import BaseModel

class MtrApprovalCodeGetSchema(BaseModel):
    approval_code:Optional[str] = None
    approval_code_name:Optional[str] = None
    
    class Config:
<<<<<<< HEAD
        orm_mode = True

class MtrApprovalCodeResponses(BaseModel):
    status_code : int
    message : str
    data : List[MtrApprovalCodeGetSchema]

class MtrApprovalCodeResponse(BaseModel):
    status_code : int
    message : str
    data : MtrApprovalCodeGetSchema
=======
        orm_mode = True
>>>>>>> 6c332901c44706e2cd630677bcf753c81a5cd6b3

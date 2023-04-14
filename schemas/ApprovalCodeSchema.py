from typing import List, Optional
from pydantic import BaseModel

class MtrApprovalCodeGetSchema(BaseModel):
    approval_code:Optional[str] = None
    approval_code_name:Optional[str] = None
    
    class Config:
        orm_mode = True

class MtrApprovalCodeResponses(BaseModel):
    status_code : int
    message : str
    data : List[MtrApprovalCodeGetSchema]

class MtrApprovalCodeResponse(BaseModel):
    status_code : int
    message : str
    data : MtrApprovalCodeGetSchema
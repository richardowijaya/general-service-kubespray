from typing import Optional, Dict
from pydantic import BaseModel
from datetime import datetime

class MtrLoggingGetSchema(BaseModel):
    created_at:datetime = None
    created_by:Optional[str] = None
    changed_at:datetime = None
    changed_by:Optional[str] = None
    hitted_api:Optional[str] = None
    http_request:Optional[str] = None
    http_response:Optional[str] = None
    data_context:Optional[str] = None
    triggered_menu:Optional[str] = None
    ip_address:Optional[str] = None

class MtrLoggingPostSchema(BaseModel):
    created_by:Optional[str] = None
    hitted_api:Optional[str] = None
    http_request:Optional[str] = None
    http_response:Optional[str] = None
    data_context:Optional[str] = None
    triggered_menu:Optional[str] = None

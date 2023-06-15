from sqlalchemy import Column, Identity,Integer,String, Boolean, DateTime
from configs.database import Base

class MtrLogging(Base):
    __tablename__ = 'mtr_logging'
    logging_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(15),nullable=False)
    changed_at = Column(DateTime, default=False)
    changed_by = Column(String(15), default=False)
    hitted_api = Column(String,nullable=False)
    http_request = Column(String(10),nullable=False)
    http_response = Column(String(10),nullable=False)
    data_context = Column(String,default=False)
    triggered_menu = Column(String(50),nullable=False)
    ip_address = Column(String(50), nullable=False)
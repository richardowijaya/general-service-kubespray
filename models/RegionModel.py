from sqlalchemy import Column,String,Integer,DateTime,Boolean,CHAR
from database.database import Base

class MtrRegion(Base):
    __tablename__ = 'mtr_region'
    is_active = Column(Boolean,nullable=False,default=True)
    regional_id = Column(Integer,primary_key=True,nullable=False)
    regional_code = Column(String(10),nullable=True)
    regional_name = Column(String(35),nullable=True)
    user_id = Column(Integer,nullable=False)
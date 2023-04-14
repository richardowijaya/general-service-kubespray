from sqlalchemy import Column,String,Integer,Boolean
from sqlalchemy.orm import relationship
from sqlmodel import SQLModel
from configs.database import Base

class MtrRegion(Base):
    __tablename__ = "mtr_region"
    is_active = Column(Boolean,nullable=False,default=True)
    region_id = Column(Integer,primary_key=True)
    region_code = Column(String(10),nullable=True)
    region_name = Column(String(35),nullable=True)
    user_id = Column(Integer,nullable=False) #relation with user table on user service

    areas = relationship("MtrArea",back_populates="region",cascade="all,delete",passive_deletes=True)

    
class MtrRegionSQL(SQLModel):
    __tablename__ = "mtr_region"
    is_active = Column(Boolean,nullable=False,default=True)
    region_id = Column(Integer,primary_key=True)
    region_code = Column(String(10),nullable=True)
    region_name = Column(String(35),nullable=True)
    user_id = Column(Integer,nullable=False) #relation with user table on user service

    areas = relationship("MtrArea",back_populates="region",cascade="all,delete",passive_deletes=True)
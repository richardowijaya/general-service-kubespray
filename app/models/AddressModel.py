from sqlalchemy import String,Column,Float,Integer, Boolean
from sqlalchemy.orm import relationship
from configs.database import Base,engine

class MtrAddress(Base):
    __tablename__ = "mtr_address"
    is_active = Column(Boolean,nullable=False,default=True)
    address_id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    address_latitude = Column(Float,nullable=True,default=0)
    address_longitude = Column(Float,nullable=True,default=0)
    address_street = Column(String(100),nullable=False)
    address_type = Column(String(5),nullable=True,default="")

    #addresses = relationship("MtrCompany",backref="mtr_address")
from sqlalchemy import Column,String,Integer,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from configs.database import Base,engine

class MtrArea(Base):
    __tablename__ = "mtr_area"
    is_active = Column(Boolean,nullable=False,default=True)
    area_id = Column(Integer,primary_key=True)
    area_code = Column(String(10),unique=True,nullable=False)
    description = Column(String,nullable=True,default="")
    region_id = Column(Integer,ForeignKey("mtr_region.region_id",ondelete="CASCADE",onupdate="CASCADE"))

    region = relationship("MtrRegion",back_populates="areas")

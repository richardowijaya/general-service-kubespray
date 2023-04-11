from sqlalchemy import CHAR, Boolean, String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from configs.database import Base, engine

class MtrArea(Base):
    __tablename__ = "mtr_area"
    is_active = Column(Boolean,nullable=False,default=True)
    area_id = Column(Integer,primary_key=True)
    area_code = Column(String(5),nullable=False)
    description = Column(String(35),nullable=True,default="")
    regional_id = Column(Integer,ForeignKey("mtr_region.regional_id",ondelete="CASCADE"))

    region = relationship("MtrRegion",back_populates="area")

MtrArea.metadata.create_all(bind=engine)
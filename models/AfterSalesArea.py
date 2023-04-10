from sqlalchemy import Column,Integer,Boolean,String
from sqlalchemy.orm import relationship
from configs.database import Base,engine

class MtrAftersalesArea(Base):
    __tablename__ = 'mtr_aftersales_area'
    is_active = Column(Boolean, nullable=False, default=True)
    aftersales_area_id = Column(Integer, nullable=False, autoincrement=True,primary_key=True)
    aftersales_area_code = Column(String(20), nullable=False, unique=True)
    aftersales_area_name = Column(String(256),nullable=True,default="")

    #aftersales_areas = relationship("MtrCompany",backref="mtr_aftersales_area")

MtrAftersalesArea.metadata.create_all(bind=engine)
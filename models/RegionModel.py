from sqlalchemy import Column,String,Integer,Boolean
from sqlalchemy.orm import relationship
from configs.database import Base,engine

class MtrRegion(Base):
    __tablename__ = "mtr_region"
    is_active = Column(Boolean,nullable=False,default=True)
    regional_id = Column(Integer,primary_key=True)
    regional_code = Column(String(10),nullable=True)
    regional_name = Column(String(35),nullable=True)
    user_id = Column(Integer,nullable=False) #relation with user table on user service

    area = relationship("MtrArea",back_populates="region",cascade="all,delete",passive_deletes=True)

MtrRegion.metadata.create_all(bind=engine)
from sqlalchemy import Column,String,Integer,Boolean
from sqlalchemy.orm import relationship
from configs.database import Base,engine

class MtrArea(Base):
    __tablename__ = "mtr_area"
    is_active = Column(Boolean,nullable=False,default=True)
    area_id = Column(Integer,primary_key=True)
    area_code = Column(String,nullable=False,unique=True)
    description = Column(String,nullable=True,default="")
    regional_id = Column(Integer,nullable=False)



MtrArea.metadata.create_all(bind=engine)
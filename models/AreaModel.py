from sqlalchemy import CHAR, Boolean, String, Column, Integer
from sqlalchemy.orm import relationship
from configs.database import Base, engine

class MtrArea(Base):
    __tablename__ = "mtr_area"
    is_active = Column(Boolean,nullable=False,default=True)
    area_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    area_code = Column(String(5),nullable=False)
    description = Column(String(35),nullable=True,defalt="")
    user_id = Column(Integer,nullable=False) #relation with user in login module/service
    
    areas = relationship("MtrCompany",backref="mtr_area")

MtrArea.metadata.create_all(bind=engine)
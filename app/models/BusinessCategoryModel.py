from sqlalchemy import Column,Boolean,String,Integer
from sqlalchemy.orm import relationship
from configs.database import Base,engine

class MtrBusinessCategory(Base):
    __tablename__ = "mtr_business_category"
    is_active = Column(Boolean,nullable=False,default=True)
    business_category_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    business_category_code = Column(String(20),nullable=False,unique=True)
    business_category_name = Column(String(256),nullable=True,default="")

    #business_categories = relationship("MtrCompany",backref="mtr_business_category")
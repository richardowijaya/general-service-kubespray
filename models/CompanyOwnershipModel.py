from sqlalchemy import Column,String,Integer,Boolean
from sqlalchemy.orm import relationship
from configs.database import Base,engine

class MtrCompanyOwnership(Base):
    __tablename__ = "mtr_company_ownership"
    is_active = Column(Boolean,nullable=False,default=True)
    company_ownership_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    company_ownership_type = Column(String(10),nullable=False,unique=True)
    company_ownership_name = Column(String(100),nullable=True,default="")

    #ownerships = relationship("MtrCompany",backref="mtr_company_ownership")

MtrCompanyOwnership.metadata.create_all(bind=engine)
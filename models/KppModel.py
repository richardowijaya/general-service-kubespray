from sqlalchemy import Boolean, String, Integer, Column
from sqlalchemy.orm import relationship
from configs.database import Base,engine

class MtrKpp(Base):
    __tablename__ = "mtr_kpp"
    is_active = Column(Boolean,nullable=False,default=True)
    kpp_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    kpp_code = Column(String(5),nullable=False,unique=True)
    kpp_name = Column(String(100),nullable=True,default="")
    kpp_phone_no = Column(String(14),nullable=True,default="")

    #kpps = relationship("MtrCompany",backref="mtr_kpp")
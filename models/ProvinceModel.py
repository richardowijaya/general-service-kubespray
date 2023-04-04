from sqlalchemy import Column, String, Integer, Boolean,ForeignKey
from configs.database import Base,engine

class MtrProvince(Base):
    __tablename__ = "mtr_province"
    is_active = Column(Boolean, nullable=False, default=True)
    province_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    province_code = Column(String(5),nullable=False,unique=True)
    province_name = Column(String(100), nullable=False)
    country_id = Column(Integer,ForeignKey("mtr_country.country_id"))

MtrProvince.metadata.create_all(bind=engine)
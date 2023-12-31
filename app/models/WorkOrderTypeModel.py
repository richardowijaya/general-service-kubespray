from sqlalchemy import Identity, String,Column,Integer, Boolean
from configs.database import Base

class MtrWorkorderType(Base):
    __tablename__ = 'mtr_work_order_type'
    

    is_active = Column(Boolean, default=True, nullable=False)
    work_order_type_id = Column(Integer, primary_key=True)
    work_order_type_code = Column(String(10), nullable=False, unique=True)
    work_order_type_name = Column(String(50), nullable=False)
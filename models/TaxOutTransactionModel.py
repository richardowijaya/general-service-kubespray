from sqlalchemy import Column,Boolean,String,Integer
from sqlalchemy.orm import relationship
from configs.database import Base, engine

class MtrTaxOutTransaction(Base):
    __tablename__ = "mtr_tax_out_transaction"
    is_active = Column(Boolean,nullable=False,default=True)
    tax_out_transaction_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    tax_out_transaction_code = Column(String(20),nullable=False)
    tax_out_transaction_name = Column(String(256),nullable=True,default="")

    tax_out_transactions = relationship("mtr_company",backref="mtr_tax_out_transaction")

MtrTaxOutTransaction.metadata.create_all(bind=engine)
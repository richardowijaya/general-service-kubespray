from sqlalchemy import CHAR,String,Integer,Boolean, Column,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from configs.database import Base,engine

class MtrCompany(Base):
    __tablename__ = "mtr_company"
    is_active = Column(Boolean,nullable=False,default="True")
    company_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    company_code = Column(String(10),nullable=False,unique=True,default="")
    company_type = Column(CHAR(1),nullable=False)
    company_name = Column(String(100),nullable=False)
    company_abbreviation = Column(String(15),nullable=False,default="")
    company_office_address_id = Column(Integer,ForeignKey("mtr_address.address.id"))
    company_phone_number = Column(String(30),nullable=True,default="")
    company_fax_number = Column(String(30,nullable=True,default=""))
    company_email = Column(String(128),nullable=True,default="")
    vat_same_company_id = Column(Integer(5),nullable=True,default=0)
    vat_npwp_no = Column(String(35),nullable=False)
    vat_npwp_date = Column(DateTime,nullable=False)
    vat_tax_out_transaction_id = Column(Integer,ForeignKey("mtr_tax_out_transaction.tax_out_transaction_id"))
    vat_tax_branch_code = Column(String(10),nullable=True,default="")
    vat_name = Column(String(100),nullable=True,default="")
    vat_address_id = Column(Integer,ForeignKey("mtr_address.address.id"))
    vat_reserve = Column(CHAR(1), nullable=True,default="")
    vat_pkp_type = Column(CHAR(1),nullable=True,default="")
    vat_pkp_no = Column(String(30),nullable=True,default="")
    vat_pkp_date = Column(DateTime,nullable=True,default="")
    vat_kpp_id = Column

    companies = relationship("MtrAddress",backref="mtr_company")

MtrCompany.metadata.create_all(bind=engine)
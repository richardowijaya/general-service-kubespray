from sqlalchemy import Boolean, Column, DateTime, Identity, Integer, String, Unicode
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TrxSpmFormRegistration(Base):
    __tablename__ = 'trx_spm_form_registration'
    __table_args__ = {'schema': 'dbo'}

    is_active = Column(Boolean, nullable=False)
    company_id = Column(Integer, nullable=False)
    register_system_number = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    registered_document_number = Column(Integer, nullable=False)
    spm_received_by = Column(Unicode(8), nullable=False)
    spm_received_date = Column(DateTime, nullable=False)
    spm_number_format = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    spm_number_from = Column(Integer, nullable=False)
    total_spm = Column(Integer, nullable=False)

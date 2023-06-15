from sqlalchemy import Boolean, CHAR, Column, DateTime, Float, ForeignKey, Identity, Integer, String, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
metadata = Base.metadata


class MtrAddress(Base):
    __tablename__ = 'mtr_address'
    __table_args__ = {'schema': 'dbo'}

    is_active = Column(Boolean, nullable=False)
    address_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    address_street = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    address_latitude = Column(Float(53))
    address_longitude = Column(Float(53))
    address_type = Column(String(5, 'SQL_Latin1_General_CP1_CI_AS'))

class MtrCompany(Base):
    __tablename__ = 'mtr_company'
    __table_args__ = {'schema': 'dbo'}

    is_active = Column(Boolean, nullable=False)
    company_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    company_code = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, unique=True)
    company_type = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    company_name = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    company_abbreviation = Column(String(15, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    vat_npwp_no = Column(String(35, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    vat_npwp_date = Column(DateTime, nullable=False)
    tax_npwp_no = Column(String(30, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    company_phone_number = Column(String(30, 'SQL_Latin1_General_CP1_CI_AS'))
    company_fax_number = Column(String(30, 'SQL_Latin1_General_CP1_CI_AS'))
    company_email = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    vat_same_company_id = Column(Integer)
    vat_tax_branch_code = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'))
    vat_name = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    vat_reserve = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    vat_pkp_type = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    vat_pkp_no = Column(String(30, 'SQL_Latin1_General_CP1_CI_AS'))
    vat_pkp_date = Column(DateTime)
    tax_npwp_data = Column(DateTime)
    tax_pkp_type = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    tax_pkp_no = Column(String(30, 'SQL_Latin1_General_CP1_CI_AS'))
    tax_pkp_date = Column(DateTime)
    company_dealer_kia_code = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'))
    company_no_of_stall = Column(Float(53))
    is_distributor = Column(Boolean)


class MtrCompanyOwnership(Base):
    __tablename__ = 'mtr_company_ownership'
    __table_args__ = {'schema': 'dbo'}

    is_active = Column(Boolean, nullable=False)
    company_ownership_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    company_ownership_type = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, unique=True)
    company_ownership_name = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))


class MtrCountry(Base):
    __tablename__ = 'mtr_country'
    __table_args__ = {'schema': 'dbo'}

    is_active = Column(Boolean, nullable=False)
    country_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    country_code = Column(String(5, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    country_name = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    country_language = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    country_phone = Column(String(15, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    currency_id = Column(Integer, nullable=False)

    mtr_province = relationship('MtrProvince', back_populates='country')

class MtrKpp(Base):
    __tablename__ = 'mtr_kpp'
    __table_args__ = {'schema': 'dbo'}

    is_active = Column(Boolean, nullable=False)
    kpp_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    kpp_code = Column(String(5, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, unique=True)
    kpp_name = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    kpp_phone_no = Column(String(14, 'SQL_Latin1_General_CP1_CI_AS'))


class MtrRegion(Base):
    __tablename__ = 'mtr_region'
    __table_args__ = {'schema': 'dbo'}

    is_active = Column(Boolean, nullable=False)
    region_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    user_id = Column(Integer, nullable=False)
    region_code = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'))
    region_name = Column(String(35, 'SQL_Latin1_General_CP1_CI_AS'))

    mtr_area = relationship('MtrArea', back_populates='regional')
    
class MtrArea(Base):
    __tablename__ = 'mtr_area'
    __table_args__ = {'schema': 'dbo'}

    is_active = Column(Boolean, nullable=False)
    area_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    area_code = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    description = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    regional_id = Column(ForeignKey('dbo.mtr_region.region_id', ondelete='CASCADE', onupdate='CASCADE'))

    regional = relationship('MtrRegion', back_populates='mtr_area')

class MtrProvince(Base):
    __tablename__ = 'mtr_province'
    __table_args__ = {'schema': 'dbo'}

    is_active = Column(Boolean, nullable=False)
    province_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    province_code = Column(String(5, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, unique=True)
    province_name = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    country_id = Column(ForeignKey('dbo.mtr_country.country_id'))

    country = relationship('MtrCountry', back_populates='mtr_province')

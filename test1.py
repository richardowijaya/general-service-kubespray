from sqlalchemy import Boolean, CHAR, Column, DateTime, Float, ForeignKey, Identity, Index, Integer, Numeric, String, Table, Unicode, text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
metadata = Base.metadata


class MtrIncentiveGroup(Base):
    __tablename__ = 'mtr_incentive_group'
    __table_args__ = {'schema': 'aftersales'}

    incentive_group_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    incentive_group_code = Column(Unicode(50), nullable=False, unique=True)
    incentive_group_name = Column(Unicode(100), nullable=False)
    effective_date = Column(DateTime, nullable=False)
    is_active = Column(Boolean, server_default=text('((1))'))

    mtr_company = relationship('MtrCompany', back_populates='incentive_group')


class MtrWarehouse(Base):
    __tablename__ = 'mtr_warehouse'
    __table_args__ = {'schema': 'aftersales'}

    warehouse_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    warehouse_code = Column(String(5, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, unique=True, server_default=text("('')"))
    address_id = Column(Integer, nullable=False)
    company_id = Column(Integer, nullable=False)
    supplier_id = Column(Integer, nullable=False)
    brand_id = Column(Integer, nullable=False)
    warehouse_group_id = Column(Integer, nullable=False)
    warehouse_person_in_charge_id = Column(Integer, nullable=False)
    warehouse_negative_stock = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    warehouse_replinishment_indicator = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    warehouse_sales_allow = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    warehouse_name = Column(Unicode(100))
    warehouse_name_detail = Column(Unicode(100))
    warehouse_intransit = Column(Boolean)
    warehouse_transit_default = Column(String(5, 'SQL_Latin1_General_CP1_CI_AS'))
    warehouse_karoseri = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    warehouse_costing_type = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    is_active = Column(Boolean, server_default=text('((1))'))

    mtr_reference = relationship('MtrReference', foreign_keys=['MtrReference.item_broken_warehouse_id'], back_populates='item_broken_warehouse')
    mtr_reference_ = relationship('MtrReference', foreign_keys=['MtrReference.unit_warehouse_id'], back_populates='unit_warehouse')


class MtrAdjustmentReason(Base):
    __tablename__ = 'mtr_adjustment_reason'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    adjustment_reason_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    adjustment_reason_code = Column(Unicode(20), unique=True)
    adjustment_reason_name = Column(Unicode(256))

    mtr_reference = relationship('MtrReference', back_populates='adjustment_reason')


class MtrAftersalesArea(Base):
    __tablename__ = 'mtr_aftersales_area'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    aftersales_area_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    aftersales_area_code = Column(Unicode(20), nullable=False, unique=True)
    aftersales_area_name = Column(Unicode(256))

    mtr_company = relationship('MtrCompany', back_populates='aftersales_area')


class MtrApprovalCode(Base):
    __tablename__ = 'mtr_approval_code'
    __table_args__ = {'schema': 'common'}

    approval_code_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    approval_code = Column(Unicode(20), nullable=False, unique=True)
    approval_code_name = Column(Unicode(256))

    mtr_approval_map = relationship('MtrApprovalMap', back_populates='approval_code')


class MtrApprovalSpm(Base):
    __tablename__ = 'mtr_approval_spm'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    approval_spm_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    approval_spm_code = Column(Unicode(20), unique=True)
    approval_spm_name = Column(Unicode(256))

    mtr_reference = relationship('MtrReference', back_populates='approval_spm')


class MtrBankAccountType(Base):
    __tablename__ = 'mtr_bank_account_type'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    bank_account_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    bank_account_type_code = Column(Unicode(20), nullable=False)
    bank_account_type_name = Column(Unicode(256))

    mtr_bank_company = relationship('MtrBankCompany', back_populates='account_type')


class MtrBusinessCategory(Base):
    __tablename__ = 'mtr_business_category'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    business_category_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    business_category_code = Column(Unicode(20), unique=True)
    business_category_name = Column(Unicode(256))

    mtr_company = relationship('MtrCompany', back_populates='business_category')


class MtrBusinessScope(Base):
    __tablename__ = 'mtr_business_scope'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    business_scope_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    business_scope_code = Column(Unicode(20), unique=True)
    business_scope_name = Column(Unicode(256))

    mtr_company = relationship('MtrCompany', back_populates='business_scope')


class MtrBusinessType(Base):
    __tablename__ = 'mtr_business_type'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    business_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    business_type_code = Column(Unicode(20), unique=True)
    business_type_name = Column(Unicode(256))

    mtr_company_brand = relationship('MtrCompanyBrand', back_populates='business_type')


class MtrFinanceArea(Base):
    __tablename__ = 'mtr_finance_area'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    finance_area_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    finance_area_code = Column(Unicode(20), nullable=False, unique=True)
    finance_area_name = Column(Unicode(256))

    mtr_company = relationship('MtrCompany', back_populates='finance_area')


class MtrJobPosition(Base):
    __tablename__ = 'mtr_job_position'
    __table_args__ = {'schema': 'common'}

    job_position_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    job_position_code = Column(Unicode(10), nullable=False, unique=True)
    job_position_description = Column(Unicode(256), nullable=False)

    mtr_user_details = relationship('MtrUserDetails', back_populates='job_position')


class MtrJobTitle(Base):
    __tablename__ = 'mtr_job_title'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False)
    job_title_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    job_title_code = Column(Unicode(5), nullable=False, unique=True)
    job_title_description = Column(Unicode(100), nullable=False)

    mtr_user_details = relationship('MtrUserDetails', back_populates='job_title')


class MtrSkillLevel(Base):
    __tablename__ = 'mtr_skill_level'
    __table_args__ = {'schema': 'common'}

    skill_level_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    skill_level_code = Column(Unicode(1), nullable=False, unique=True)

    mtr_user_details = relationship('MtrUserDetails', back_populates='skill_level')


class MtrSourceApprovalDocument(Base):
    __tablename__ = 'mtr_source_approval_document'
    __table_args__ = {'schema': 'common'}

    source_approval_document_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    source_approval_document_code = Column(Unicode(20), nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False)
    source_approval_document_name = Column(Unicode(256))

    mtr_approval_map = relationship('MtrApprovalMap', back_populates='source_approval_document')
    mtr_source_document = relationship('MtrSourceDocument', back_populates='source_approval_document')
    mtr_source_document_detail = relationship('MtrSourceDocumentDetail', back_populates='source_approval_document')


class MtrTaxOutTransaction(Base):
    __tablename__ = 'mtr_tax_out_transaction'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    tax_out_transaction_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    tax_out_transaction_code = Column(Unicode(20), nullable=False, unique=True)
    tax_out_transaction_name = Column(Unicode(256))

    mtr_vat_company = relationship('MtrVatCompany', back_populates='tax_out_transaction')


class MtrTransactionType(Base):
    __tablename__ = 'mtr_transaction_type'
    __table_args__ = {'schema': 'common'}

    transaction_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    transaction_type_code = Column(Unicode(20), nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False)
    transaction_type_name = Column(Unicode(256))

    mtr_approval_map = relationship('MtrApprovalMap', back_populates='transaction_type')
    mtr_source_document = relationship('MtrSourceDocument', back_populates='transaction_type')
    mtr_source_document_detail = relationship('MtrSourceDocumentDetail', back_populates='transaction_type')


class MtrVoidTransaction(Base):
    __tablename__ = 'mtr_void_transaction'
    __table_args__ = {'schema': 'common'}

    void_transaction_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    void_transaction_code = Column(Unicode(20), nullable=False, unique=True)
    void_transaction_name = Column(Unicode(256))

    mtr_approval_map = relationship('MtrApprovalMap', back_populates='void_transaction')


class MtrBank(Base):
    __tablename__ = 'mtr_bank'
    __table_args__ = {'schema': 'finance'}

    bank_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    bank_code = Column(Integer, nullable=False, unique=True)
    is_active = Column(Boolean, server_default=text('((1))'))
    bank_name = Column(Unicode(100))
    bank_abbr = Column(Unicode(100))

    mtr_bank_branch = relationship('MtrBankBranch', back_populates='bank')
    mtr_bank_company = relationship('MtrBankCompany', back_populates='bank')


class MtrCoaGroup(Base):
    __tablename__ = 'mtr_coa_group'
    __table_args__ = {'schema': 'finance'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    coa_group_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    coa_group_code = Column(Unicode(15), nullable=False, unique=True)
    coa_group_name = Column(Unicode(128), nullable=False)

    mtr_reference = relationship('MtrReference', back_populates='coa_group')


class MtrCurrency(Base):
    __tablename__ = 'mtr_currency'
    __table_args__ = {'schema': 'finance'}

    currency_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    currency_code = Column(CHAR(3, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, unique=True)
    currency_name = Column(Unicode(35), nullable=False)
    currency_round_digit = Column(Numeric(2, 0), nullable=False, server_default=text('((0))'))
    currency_round_method = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    currency_unit = Column(Unicode(20), nullable=False)
    currency_fraction = Column(Unicode(20), nullable=False)
    is_active = Column(Boolean, server_default=text('((1))'))
    company_bank_format_type = Column(Numeric(2, 0))

    mtr_bank_company = relationship('MtrBankCompany', back_populates='currency')
    mtr_reference = relationship('MtrReference', back_populates='currency')


class MtrProfitCenterBusinessCategory(Base):
    __tablename__ = 'mtr_profit_center_business_category'
    __table_args__ = {'schema': 'finance'}

    profit_center_business_category_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    business_category_id = Column(Integer, nullable=False)
    is_active = Column(Boolean, server_default=text('((1))'))

    mtr_profit_center = relationship('MtrProfitCenter', back_populates='profit_center_business_category')
    mtr_bank_company = relationship('MtrBankCompany', back_populates='profit_center_business_category')


class MtrApprovalTemplate(Base):
    __tablename__ = 'mtr_approval_template'
    __table_args__ = {'schema': 'general'}

    approval_code_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    approval_code = Column(Unicode(20), nullable=False, unique=True)
    company_id = Column(ForeignKey('general.mtr_company.company_id'), nullable=False)
    approval_name = Column(Unicode(100), nullable=False)
    module_description_id = Column(ForeignKey('general.mtr_module_description.module_description_id'), nullable=False)
    source_doc_type_id = Column(ForeignKey('general.mtr_source_doc_type.source_doc_type_id'))
    is_active = Column(Boolean)

    company = relationship('MtrCompany', back_populates='mtr_approval_template')
    module_description = relationship('MtrModuleDescription', back_populates='mtr_approval_template')
    source_doc_type = relationship('MtrSourceDocType', foreign_keys=[source_doc_type_id], back_populates='mtr_approval_template')
    mtr_source_doc_type = relationship('MtrSourceDocType', foreign_keys=['MtrSourceDocType.approval_code_id'], back_populates='approval_code')
    mtr_approval_code_description = relationship('MtrApprovalCodeDescription', back_populates='approval_code')


class MtrCompany(Base):
    __tablename__ = 'mtr_company'
    __table_args__ = {'schema': 'general'}

    company_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    company_code = Column(Unicode(10), nullable=False, unique=True)
    company_type = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    company_name = Column(Unicode(100), nullable=False)
    company_abbreviation = Column(Unicode(15), nullable=False)
    company_office_address_id = Column(ForeignKey('general.mtr_address.address_id'), nullable=False)
    vat_company_id = Column(ForeignKey('general.mtr_vat_company.vat_company_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    tax_npwp_no = Column(Unicode(30), nullable=False)
    tax_address_id = Column(ForeignKey('general.mtr_address.address_id'), nullable=False)
    region_id = Column(ForeignKey('general.mtr_region.region_id'), nullable=False)
    finance_area_id = Column(ForeignKey('common.mtr_finance_area.finance_area_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    area_id = Column(ForeignKey('general.mtr_area.area_id'), nullable=False)
    incentive_group_id = Column(ForeignKey('aftersales.mtr_incentive_group.incentive_group_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    aftersales_area_id = Column(ForeignKey('common.mtr_aftersales_area.aftersales_area_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    company_ownership_id = Column(ForeignKey('general.mtr_company_ownership.company_ownership_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    business_category_id = Column(ForeignKey('common.mtr_business_category.business_category_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    business_scope_id = Column(ForeignKey('common.mtr_business_scope.business_scope_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    term_of_payment_id = Column(ForeignKey('general.mtr_term_of_payment.term_of_payment_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    is_active = Column(Boolean, server_default=text('((1))'))
    company_phone_number = Column(Unicode(30))
    company_fax_number = Column(Unicode(30))
    company_email = Column(Unicode(128))
    tax_npwp_date = Column(DateTime)
    tax_name = Column(Unicode(100))
    tax_pkp_type = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    tax_pkp_no = Column(Unicode(30))
    tax_pkp_date = Column(DateTime)
    tax_kpp_id = Column(ForeignKey('general.mtr_kpp.kpp_id'))
    company_dealer_kia_code = Column(Unicode(10))
    company_no_of_stall = Column(Numeric(3, 0), server_default=text('((0))'))
    is_distributor = Column(Boolean, server_default=text('((0))'))

    mtr_approval_template = relationship('MtrApprovalTemplate', back_populates='company')
    aftersales_area = relationship('MtrAftersalesArea', back_populates='mtr_company')
    area = relationship('MtrArea', back_populates='mtr_company')
    business_category = relationship('MtrBusinessCategory', back_populates='mtr_company')
    business_scope = relationship('MtrBusinessScope', back_populates='mtr_company')
    company_office_address = relationship('MtrAddress', foreign_keys=[company_office_address_id], back_populates='mtr_company')
    company_ownership = relationship('MtrCompanyOwnership', back_populates='mtr_company')
    finance_area = relationship('MtrFinanceArea', back_populates='mtr_company')
    incentive_group = relationship('MtrIncentiveGroup', back_populates='mtr_company')
    region = relationship('MtrRegion', back_populates='mtr_company')
    tax_address = relationship('MtrAddress', foreign_keys=[tax_address_id], back_populates='mtr_company_')
    tax_kpp = relationship('MtrKpp', back_populates='mtr_company')
    term_of_payment = relationship('MtrTermOfPayment', back_populates='mtr_company')
    vat_company = relationship('MtrVatCompany', foreign_keys=[vat_company_id], back_populates='mtr_company')
    mtr_vat_company = relationship('MtrVatCompany', foreign_keys=['MtrVatCompany.company_id'], back_populates='company')
    mtr_approval_group = relationship('MtrApprovalGroup', back_populates='company')
    mtr_company_brand = relationship('MtrCompanyBrand', back_populates='company')
    mtr_company_head_office = relationship('MtrCompanyHeadOffice', back_populates='company')
    mtr_news = relationship('MtrNews', back_populates='company')
    mtr_user_company_access = relationship('MtrUserCompanyAccess', back_populates='company')
    mtr_dealer_representative = relationship('MtrDealerRepresentative', back_populates='company')
    mtr_cost_profit_map = relationship('MtrCostProfitMap', back_populates='company')
    mtr_user_details = relationship('MtrUserDetails', back_populates='company')
    mtr_bank_company = relationship('MtrBankCompany', back_populates='company')
    mtr_employee_group = relationship('MtrEmployeeGroup', back_populates='company')
    mtr_supplier_reference = relationship('MtrSupplierReference', back_populates='company')
    mtr_customer_va_dbs = relationship('MtrCustomerVaDbs', back_populates='company')
    mtr_reference = relationship('MtrReference', back_populates='company')
    mtr_source_document_detail = relationship('MtrSourceDocumentDetail', back_populates='company')


class MtrCompanyOwnership(Base):
    __tablename__ = 'mtr_company_ownership'
    __table_args__ = {'schema': 'general'}

    company_ownership_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, server_default=text('((1))'))
    company_ownership_type = Column(Unicode(10), unique=True)
    company_ownership_name = Column(Unicode(100))

    mtr_company = relationship('MtrCompany', back_populates='company_ownership')


class MtrCostCenter(Base):
    __tablename__ = 'mtr_cost_center'
    __table_args__ = {'schema': 'general'}

    cost_center_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    cost_center_code = Column(Unicode(5), nullable=False, unique=True)
    cost_center_name = Column(Unicode(100))
    is_active = Column(Boolean, server_default=text('((1))'))

    mtr_approval_map = relationship('MtrApprovalMap', back_populates='cost_center')
    mtr_cost_profit_map = relationship('MtrCostProfitMap', back_populates='cost_center')
    mtr_user_details = relationship('MtrUserDetails', back_populates='cost_center')
    mtr_bank_company = relationship('MtrBankCompany', back_populates='cost_center')


class MtrCountry(Base):
    __tablename__ = 'mtr_country'
    __table_args__ = {'schema': 'general'}

    country_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    country_code = Column(Unicode(5), nullable=False, unique=True)
    currency_id = Column(Integer, nullable=False)
    country_name = Column(Unicode(100))
    country_language = Column(Unicode(20))
    country_phone_area = Column(Unicode(4))
    is_active = Column(Boolean, server_default=text('((1))'))

    mtr_province = relationship('MtrProvince', back_populates='country')


class MtrCustomerType(Base):
    __tablename__ = 'mtr_customer_type'
    __table_args__ = {'schema': 'general'}

    customer_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    customer_type = Column(CHAR(2, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, unique=True)
    customer_type_description = Column(Unicode(35), nullable=False)
    customer_type_flag = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    customer_type_group = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    spm = Column(Boolean, nullable=False, server_default=text('((0))'))
    bbn = Column(Boolean, nullable=False, server_default=text('((0))'))
    police_invoice = Column(Boolean, nullable=False, server_default=text('((0))'))
    tax_free = Column(Boolean, nullable=False, server_default=text('((0))'))
    is_active = Column(Boolean, server_default=text('((1))'))


class MtrDivision(Base):
    __tablename__ = 'mtr_division'
    __table_args__ = {'schema': 'general'}

    division_id = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    division_code = Column(CHAR(3, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, unique=True)
    division_name = Column(Unicode(50), nullable=False)
    is_active = Column(Boolean, nullable=False)

    mtr_user_details = relationship('MtrUserDetails', back_populates='division')
    mtr_supplier_pic = relationship('MtrSupplierPic', back_populates='pic_division')
    mtr_supplier_reference_pic = relationship('MtrSupplierReferencePic', back_populates='pic_division')


t_mtr_logging = Table(
    'mtr_logging', metadata,
    Column('created_at', DateTime),
    Column('created_by', Unicode(5)),
    Column('changed_at', DateTime),
    Column('changed_by', Unicode(5)),
    Column('hit_API', Unicode(100)),
    Column('action', Unicode(10)),
    Column('context', Unicode(20)),
    Column('triggered_menu', Unicode(30)),
    Column('ip_address', Unicode(30)),
    schema='general'
)


class MtrModuleDescription(Base):
    __tablename__ = 'mtr_module_description'
    __table_args__ = {'schema': 'general'}

    module_description_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    module_description_code = Column(Unicode(5), nullable=False, unique=True)
    module_description = Column(Unicode(50), nullable=False)

    mtr_approval_template = relationship('MtrApprovalTemplate', back_populates='module_description')


class MtrSourceDocType(Base):
    __tablename__ = 'mtr_source_doc_type'
    __table_args__ = {'schema': 'general'}

    source_doc_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    approval_code_id = Column(ForeignKey('general.mtr_approval_template.approval_code_id'), nullable=False)
    source_doc_type_description = Column(Integer, nullable=False)

    mtr_approval_template = relationship('MtrApprovalTemplate', foreign_keys=['MtrApprovalTemplate.source_doc_type_id'], back_populates='source_doc_type')
    approval_code = relationship('MtrApprovalTemplate', foreign_keys=[approval_code_id], back_populates='mtr_source_doc_type')


class MtrStorageType(Base):
    __tablename__ = 'mtr_storage_type'
    __table_args__ = {'schema': 'general'}

    storage_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    storage_type_code = Column(Unicode(10), nullable=False, unique=True)
    storage_type_name = Column(Unicode(100))
    is_active = Column(Boolean, server_default=text('((1))'))


class MtrSupplierCoaGroupMapping(Base):
    __tablename__ = 'mtr_supplier_coa_group_mapping'
    __table_args__ = {'schema': 'general'}

    group_mapping_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    coa_group_id = Column(Integer, nullable=False)
    supplier_prefix = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class MtrSupplierEmployee(Base):
    __tablename__ = 'mtr_supplier_employee'
    __table_args__ = {'schema': 'general'}

    supplier_employee_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    employee_id = Column(Integer)


class MtrSupplierType(Base):
    __tablename__ = 'mtr_supplier_type'
    __table_args__ = {'schema': 'general'}

    supplier_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    supplier_type = Column(Unicode(5), nullable=False, server_default=text("('')"))
    description = Column(Unicode(35), server_default=text("('')"))
    group = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))

    mtr_supplier = relationship('MtrSupplier', back_populates='supplier_type')
    mtr_supplier_reference = relationship('MtrSupplierReference', back_populates='supplier_type')


class MtrTermOfPayment(Base):
    __tablename__ = 'mtr_term_of_payment'
    __table_args__ = {'schema': 'general'}

    term_of_payment_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    term_of_payment_code = Column(Unicode(5), nullable=False, unique=True)
    term_of_payment_name = Column(Unicode(100))
    is_active = Column(Boolean, server_default=text('((1))'))
    term_of_payment_policy = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    term_of_payment_installment = Column(Integer)
    term_of_payment_interval = Column(Integer)

    mtr_company = relationship('MtrCompany', back_populates='term_of_payment')
    mtr_supplier = relationship('MtrSupplier', back_populates='term_of_payment')
    mtr_supplier_reference = relationship('MtrSupplierReference', back_populates='term_of_payment')


class MtrVatCompany(Base):
    __tablename__ = 'mtr_vat_company'
    __table_args__ = {'schema': 'general'}

    vat_company_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    company_id = Column(ForeignKey('general.mtr_company.company_id'), nullable=False)
    vat_npwp_no = Column(Unicode(30), nullable=False, unique=True)
    vat_npwp_date = Column(DateTime, nullable=False)
    tax_out_transaction_id = Column(ForeignKey('common.mtr_tax_out_transaction.tax_out_transaction_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    address_id = Column(ForeignKey('general.mtr_address.address_id'), nullable=False)
    kpp_id = Column(ForeignKey('general.mtr_kpp.kpp_id'), nullable=False)
    vat_tax_branch_code = Column(Unicode(10))
    vat_name = Column(Unicode(100))
    vat_reserve = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    vat_pkp_type = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    vat_pkp_no = Column(Unicode(30))
    vat_pkp_date = Column(DateTime)

    mtr_company = relationship('MtrCompany', foreign_keys=['MtrCompany.vat_company_id'], back_populates='vat_company')
    address = relationship('MtrAddress', back_populates='mtr_vat_company')
    company = relationship('MtrCompany', foreign_keys=[company_id], back_populates='mtr_vat_company')
    kpp = relationship('MtrKpp', back_populates='mtr_vat_company')
    tax_out_transaction = relationship('MtrTaxOutTransaction', back_populates='mtr_vat_company')


class UserLogin(Base):
    __tablename__ = 'user_login'
    __table_args__ = {'schema': 'general'}

    user_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    last_login = Column(DateTime, nullable=False)
    user_name = Column(Unicode(100))
    password = Column(Unicode(128))
    is_active = Column(Boolean, server_default=text('((1))'))

    mtr_approval_group = relationship('MtrApprovalGroup', back_populates='user')
    mtr_region = relationship('MtrRegion', back_populates='user')
    mtr_user_company_access = relationship('MtrUserCompanyAccess', back_populates='user')
    mtr_user_details = relationship('MtrUserDetails', back_populates='user')


class MtrBrand(Base):
    __tablename__ = 'mtr_brand'
    __table_args__ = (
        Index('mtr_brand_UN', 'brand_code', 'brand_name', 'brand_abbreviation', unique=True),
        {'schema': 'sales'}
    )

    brand_id = Column(Integer, primary_key=True)
    brand_code = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    supplier_id = Column(Integer, nullable=False)
    warehouse_id = Column(Integer, nullable=False)
    brand_abbreviation = Column(String(2, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    brand_name = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    brand_must_withdrawal = Column(Boolean)
    brand_must_pdi = Column(Boolean)
    atpm_unit = Column(Boolean)
    atpm_workshop = Column(Boolean)
    atpm_sparepart = Column(Boolean)
    atpm_finance = Column(Boolean)

    mtr_company_brand = relationship('MtrCompanyBrand', back_populates='brand')
    mtr_approval_map = relationship('MtrApprovalMap', back_populates='brand')
    mtr_bank_company = relationship('MtrBankCompany', back_populates='brand')
    mtr_source_document = relationship('MtrSourceDocument', back_populates='brand')
    mtr_source_document_detail = relationship('MtrSourceDocumentDetail', back_populates='brand')


class MtrApprovalCodeDescription(Base):
    __tablename__ = 'mtr_approval_code_description'
    __table_args__ = {'schema': 'general'}

    approval_code_description_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    approval_code_id = Column(ForeignKey('general.mtr_approval_template.approval_code_id'), nullable=False)
    approval_code_description = Column(Unicode(100), nullable=False)

    approval_code = relationship('MtrApprovalTemplate', back_populates='mtr_approval_code_description')


class MtrApprovalGroup(Base):
    __tablename__ = 'mtr_approval_group'
    __table_args__ = {'schema': 'general'}

    approver_group_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    approver_group_code = Column(Unicode(10), nullable=False, unique=True)
    approver_group_name = Column(Unicode(100), nullable=False)
    company_id = Column(ForeignKey('general.mtr_company.company_id'), nullable=False)
    user_id = Column(ForeignKey('general.user_login.user_id'), nullable=False)
    is_active = Column(Boolean)

    company = relationship('MtrCompany', back_populates='mtr_approval_group')
    user = relationship('UserLogin', back_populates='mtr_approval_group')


class MtrCompanyBrand(Base):
    __tablename__ = 'mtr_company_brand'
    __table_args__ = {'schema': 'general'}

    company_brand_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    company_id = Column(ForeignKey('general.mtr_company.company_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    brand_id = Column(ForeignKey('sales.mtr_brand.brand_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    business_type_id = Column(ForeignKey('common.mtr_business_type.business_type_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    generate_acc_po = Column(Boolean, nullable=False, server_default=text('((0))'))
    is_active = Column(Boolean, server_default=text('((1))'))
    atmp_dealer_code = Column(Unicode(18))
    print_from_name = Column(Unicode(100))

    brand = relationship('MtrBrand', back_populates='mtr_company_brand')
    business_type = relationship('MtrBusinessType', back_populates='mtr_company_brand')
    company = relationship('MtrCompany', back_populates='mtr_company_brand')


class MtrCompanyHeadOffice(Base):
    __tablename__ = 'mtr_company_head_office'
    __table_args__ = {'schema': 'general'}

    company_head_office_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    company_head_office_code = Column(Unicode(10), nullable=False, unique=True)
    company_id = Column(ForeignKey('general.mtr_company.company_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    company = relationship('MtrCompany', back_populates='mtr_company_head_office')


class MtrNews(Base):
    __tablename__ = 'mtr_news'
    __table_args__ = {'schema': 'general'}

    news_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, server_default=text('((1))'))
    news_title = Column(Unicode(100))
    news_headline = Column(Unicode(100))
    news_detail = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    news_date = Column(DateTime)
    company_id = Column(ForeignKey('general.mtr_company.company_id'))

    company = relationship('MtrCompany', back_populates='mtr_news')


class MtrProfitCenter(Base):
    __tablename__ = 'mtr_profit_center'
    __table_args__ = {'schema': 'general'}

    profit_center_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    profit_center_code = Column(Unicode(5), nullable=False, unique=True)
    profit_center_business_category_id = Column(ForeignKey('finance.mtr_profit_center_business_category.profit_center_business_category_id'), nullable=False)
    profit_center_name = Column(Unicode(100))
    is_active = Column(Boolean, server_default=text('((1))'))

    profit_center_business_category = relationship('MtrProfitCenterBusinessCategory', back_populates='mtr_profit_center')
    mtr_approval_map = relationship('MtrApprovalMap', back_populates='profit_center')
    mtr_cost_profit_map = relationship('MtrCostProfitMap', back_populates='profit_center')
    mtr_user_details = relationship('MtrUserDetails', back_populates='profit_center')
    mtr_source_document = relationship('MtrSourceDocument', back_populates='profit_center')
    mtr_source_document_detail = relationship('MtrSourceDocumentDetail', back_populates='profit_center')


class MtrProvince(Base):
    __tablename__ = 'mtr_province'
    __table_args__ = {'schema': 'general'}

    province_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    province_code = Column(Unicode(5), nullable=False, unique=True)
    country_id = Column(ForeignKey('general.mtr_country.country_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    province_name = Column(Unicode(100))
    is_active = Column(Boolean, server_default=text('((1))'))

    country = relationship('MtrCountry', back_populates='mtr_province')
    mtr_city = relationship('MtrCity', back_populates='province')


class MtrRegion(Base):
    __tablename__ = 'mtr_region'
    __table_args__ = {'schema': 'general'}

    region_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    region_code = Column(Unicode(10), nullable=False)
    region_name = Column(Unicode(35), nullable=False)
    user_id = Column(ForeignKey('general.user_login.user_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    is_active = Column(Boolean, nullable=False)

    mtr_company = relationship('MtrCompany', back_populates='region')
    user = relationship('UserLogin', back_populates='mtr_region')
    mtr_area = relationship('MtrArea', back_populates='region')


class MtrUserCompanyAccess(Base):
    __tablename__ = 'mtr_user_company_access'
    __table_args__ = {'schema': 'general'}

    mtr_user_company_access_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    user_id = Column(ForeignKey('general.user_login.user_id'), nullable=False)
    company_id = Column(ForeignKey('general.mtr_company.company_id'), nullable=False)

    company = relationship('MtrCompany', back_populates='mtr_user_company_access')
    user = relationship('UserLogin', back_populates='mtr_user_company_access')


class MtrApprovalMap(Base):
    __tablename__ = 'mtr_approval_map'
    __table_args__ = (
        Index('mtr_approval_map_UN', 'source_approval_document_id', 'transaction_type_id', 'brand_id', 'cost_center_id', 'profit_center_id', 'void_transaction_id', 'approval_code_id', unique=True),
        {'schema': 'general'}
    )

    approval_map_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    source_approval_document_id = Column(ForeignKey('common.mtr_source_approval_document.source_approval_document_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    transaction_type_id = Column(ForeignKey('common.mtr_transaction_type.transaction_type_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    brand_id = Column(ForeignKey('sales.mtr_brand.brand_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    cost_center_id = Column(ForeignKey('general.mtr_cost_center.cost_center_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    profit_center_id = Column(ForeignKey('general.mtr_profit_center.profit_center_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    void_transaction_id = Column(ForeignKey('common.mtr_void_transaction.void_transaction_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    approval_code_id = Column(ForeignKey('common.mtr_approval_code.approval_code_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    is_active = Column(Boolean, nullable=False)

    approval_code = relationship('MtrApprovalCode', back_populates='mtr_approval_map')
    brand = relationship('MtrBrand', back_populates='mtr_approval_map')
    cost_center = relationship('MtrCostCenter', back_populates='mtr_approval_map')
    profit_center = relationship('MtrProfitCenter', back_populates='mtr_approval_map')
    source_approval_document = relationship('MtrSourceApprovalDocument', back_populates='mtr_approval_map')
    transaction_type = relationship('MtrTransactionType', back_populates='mtr_approval_map')
    void_transaction = relationship('MtrVoidTransaction', back_populates='mtr_approval_map')


class MtrArea(Base):
    __tablename__ = 'mtr_area'
    __table_args__ = {'schema': 'general'}

    area_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    area_code = Column(Unicode(5), nullable=False, unique=True)
    region_id = Column(ForeignKey('general.mtr_region.region_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    is_active = Column(Boolean, server_default=text('((1))'))
    description = Column(Unicode(35), server_default=text('(NULL)'))

    mtr_company = relationship('MtrCompany', back_populates='area')
    region = relationship('MtrRegion', back_populates='mtr_area')


class MtrCity(Base):
    __tablename__ = 'mtr_city'
    __table_args__ = {'schema': 'general'}

    city_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    city_code = Column(Unicode(5), nullable=False, unique=True)
    province_id = Column(ForeignKey('general.mtr_province.province_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    city_name = Column(Unicode(100))
    city_phone_area = Column(Unicode(5))
    is_active = Column(Boolean, server_default=text('((1))'))

    province = relationship('MtrProvince', back_populates='mtr_city')
    mtr_dealer_representative = relationship('MtrDealerRepresentative', back_populates='city')
    mtr_district = relationship('MtrDistrict', back_populates='city')
    mtr_user_details = relationship('MtrUserDetails', back_populates='mtr_city')


class MtrDealerRepresentative(Base):
    __tablename__ = 'mtr_dealer_representative'
    __table_args__ = (
        Index('mtr_dealer_representative_UN', 'dealer_representative_code', 'dealer_representative_cost_center_sequence', unique=True),
        {'schema': 'general'}
    )

    dealer_representative_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    city_id = Column(ForeignKey('general.mtr_city.city_id'), nullable=False)
    company_id = Column(ForeignKey('general.mtr_company.company_id'), nullable=False)
    is_active = Column(Boolean, server_default=text('((1))'))
    dealer_representative_code = Column(Integer)
    dealer_representative_name = Column(Unicode(128), server_default=text("('')"))
    dealer_representative_cost_center_sequence = Column(Integer)

    city = relationship('MtrCity', back_populates='mtr_dealer_representative')
    company = relationship('MtrCompany', back_populates='mtr_dealer_representative')
    mtr_cost_profit_map = relationship('MtrCostProfitMap', back_populates='dealer_rep')


class MtrDistrict(Base):
    __tablename__ = 'mtr_district'
    __table_args__ = {'schema': 'general'}

    district_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    district_code = Column(Unicode(5), nullable=False, unique=True)
    city_id = Column(ForeignKey('general.mtr_city.city_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    district_name = Column(Unicode(100))
    is_active = Column(Boolean, server_default=text('((1))'))

    city = relationship('MtrCity', back_populates='mtr_district')
    mtr_village = relationship('MtrVillage', back_populates='district')


class MtrCostProfitMap(Base):
    __tablename__ = 'mtr_cost_profit_map'
    __table_args__ = {'schema': 'general'}

    cost_profit_map_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    cost_center_id = Column(ForeignKey('general.mtr_cost_center.cost_center_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    profit_center_id = Column(ForeignKey('general.mtr_profit_center.profit_center_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    company_id = Column(ForeignKey('general.mtr_company.company_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    dealer_rep_id = Column(ForeignKey('general.mtr_dealer_representative.dealer_representative_id'), nullable=False)
    cost_profit_name = Column(Unicode(100))
    is_active = Column(Boolean, server_default=text('((1))'))

    company = relationship('MtrCompany', back_populates='mtr_cost_profit_map')
    cost_center = relationship('MtrCostCenter', back_populates='mtr_cost_profit_map')
    dealer_rep = relationship('MtrDealerRepresentative', back_populates='mtr_cost_profit_map')
    profit_center = relationship('MtrProfitCenter', back_populates='mtr_cost_profit_map')


class MtrVillage(Base):
    __tablename__ = 'mtr_village'
    __table_args__ = {'schema': 'general'}

    village_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    village_code = Column(Unicode(5), nullable=False, unique=True)
    district_id = Column(ForeignKey('general.mtr_district.district_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    village_name = Column(Unicode(100))
    is_active = Column(Boolean, server_default=text('((1))'))
    village_zip_code = Column(Unicode(10))

    district = relationship('MtrDistrict', back_populates='mtr_village')
    mtr_address = relationship('MtrAddress', back_populates='village')


class MtrAddress(Base):
    __tablename__ = 'mtr_address'
    __table_args__ = {'schema': 'general'}

    address_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    village_id = Column(ForeignKey('general.mtr_village.village_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    address_type = Column(Unicode(5), nullable=False)
    address_street = Column(Unicode(100))
    address_longitude = Column(Float(53))
    address_latitude = Column(Float(53))
    is_active = Column(Boolean, server_default=text('((1))'))

    mtr_company = relationship('MtrCompany', foreign_keys=['MtrCompany.company_office_address_id'], back_populates='company_office_address')
    mtr_company_ = relationship('MtrCompany', foreign_keys=['MtrCompany.tax_address_id'], back_populates='tax_address')
    mtr_vat_company = relationship('MtrVatCompany', back_populates='address')
    village = relationship('MtrVillage', back_populates='mtr_address')
    mtr_bank_branch = relationship('MtrBankBranch', back_populates='address')
    mtr_income_tax = relationship('MtrIncomeTax', back_populates='address')
    mtr_kpp = relationship('MtrKpp', back_populates='address')
    mtr_user_details = relationship('MtrUserDetails', back_populates='address')
    mtr_supplier = relationship('MtrSupplier', foreign_keys=['MtrSupplier.supplier_address_id'], back_populates='supplier_address')
    mtr_supplier_ = relationship('MtrSupplier', foreign_keys=['MtrSupplier.tax_address_id'], back_populates='tax_address')
    mtr_supplier1 = relationship('MtrSupplier', foreign_keys=['MtrSupplier.vat_address_id'], back_populates='vat_address')
    mtr_supplier_reference = relationship('MtrSupplierReference', foreign_keys=['MtrSupplierReference.supplier_address_id'], back_populates='supplier_address')
    mtr_supplier_reference_ = relationship('MtrSupplierReference', foreign_keys=['MtrSupplierReference.tax_address_id'], back_populates='tax_address')
    mtr_supplier_reference1 = relationship('MtrSupplierReference', foreign_keys=['MtrSupplierReference.vat_address_id'], back_populates='vat_address')


class MtrBankBranch(Base):
    __tablename__ = 'mtr_bank_branch'
    __table_args__ = {'schema': 'finance'}

    bank_branch_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    bank_branch_code = Column(Integer, nullable=False, unique=True)
    bank_id = Column(ForeignKey('finance.mtr_bank.bank_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    address_id = Column(ForeignKey('general.mtr_address.address_id'), nullable=False)
    is_active = Column(Boolean, server_default=text('((1))'))
    bank_branch_name = Column(Unicode(100))

    address = relationship('MtrAddress', back_populates='mtr_bank_branch')
    bank = relationship('MtrBank', back_populates='mtr_bank_branch')
    mtr_bank_company = relationship('MtrBankCompany', back_populates='bank_branch')


class MtrIncomeTax(Base):
    __tablename__ = 'mtr_income_tax'
    __table_args__ = {'schema': 'general'}

    income_tax_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    income_tax_npwp_no = Column(Unicode(30), nullable=False, unique=True)
    address_id = Column(ForeignKey('general.mtr_address.address_id'), nullable=False)
    income_tax_pkp_type = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    kpp_id = Column(Integer, nullable=False)
    is_active = Column(Boolean, server_default=text('((1))'))
    income_tax_npwp_date = Column(DateTime)
    income_tax_name = Column(Unicode(100))
    income_tax_pkp_no = Column(Unicode(30))
    income_tax_pkp_date = Column(DateTime)

    address = relationship('MtrAddress', back_populates='mtr_income_tax')


class MtrKpp(Base):
    __tablename__ = 'mtr_kpp'
    __table_args__ = {'schema': 'general'}

    kpp_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    kpp_code = Column(Unicode(5), nullable=False)
    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    address_id = Column(ForeignKey('general.mtr_address.address_id'), nullable=False, unique=True)
    kpp_name = Column(Unicode(100))
    kpp_phone_no = Column(Unicode(14))

    mtr_company = relationship('MtrCompany', back_populates='tax_kpp')
    mtr_vat_company = relationship('MtrVatCompany', back_populates='kpp')
    address = relationship('MtrAddress', back_populates='mtr_kpp')
    mtr_supplier = relationship('MtrSupplier', foreign_keys=['MtrSupplier.tax_kpp_id'], back_populates='tax_kpp')
    mtr_supplier_ = relationship('MtrSupplier', foreign_keys=['MtrSupplier.vat_kpp_id'], back_populates='vat_kpp')
    mtr_supplier_reference = relationship('MtrSupplierReference', foreign_keys=['MtrSupplierReference.tax_kpp_id'], back_populates='tax_kpp')
    mtr_supplier_reference_ = relationship('MtrSupplierReference', foreign_keys=['MtrSupplierReference.vat_kpp_id'], back_populates='vat_kpp')


class MtrUserDetails(Base):
    __tablename__ = 'mtr_user_details'
    __table_args__ = {'schema': 'general'}

    is_active = Column(Boolean, nullable=False)
    user_employee_id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('general.user_login.user_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    employee_name = Column(Unicode(30), nullable=False)
    company_id = Column(ForeignKey('general.mtr_company.company_id'), nullable=False)
    job_title_id = Column(ForeignKey('common.mtr_job_title.job_title_id'), nullable=False)
    job_position_id = Column(ForeignKey('common.mtr_job_position.job_position_id'), nullable=False)
    division_id = Column(ForeignKey('general.mtr_division.division_id'), nullable=False)
    cost_center_id = Column(ForeignKey('general.mtr_cost_center.cost_center_id'), nullable=False)
    profit_center_id = Column(ForeignKey('general.mtr_profit_center.profit_center_id'), nullable=False)
    address_id = Column(ForeignKey('general.mtr_address.address_id'), nullable=False)
    email_address = Column(Unicode(100), nullable=False)
    gender = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    city_of_birth = Column(ForeignKey('general.mtr_city.city_id'), nullable=False)
    marital_status = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    user_bank_account_id = Column(Integer, nullable=False)
    employee_nickname = Column(Unicode(20), server_default=text('(NULL)'))
    skill_level_id = Column(ForeignKey('common.mtr_skill_level.skill_level_id'), server_default=text('((0))'))
    factor_x = Column(Numeric(2, 0), server_default=text('((0))'))
    office_phone_no = Column(Unicode(30), server_default=text('(NULL)'))
    home_phone_no = Column(Unicode(30), server_default=text('(NULL)'))
    mobile_phone = Column(Unicode(30), server_default=text('(NULL)'))
    start_date = Column(DateTime, server_default=text('(NULL)'))
    termination_date = Column(DateTime, server_default=text('(NULL)'))
    no_of_children = Column(Integer, server_default=text('((0))'))
    id_type = Column(Unicode(10), server_default=text('(NULL)'))
    id_no = Column(Unicode(35), server_default=text('(NULL)'))
    citizenship = Column(Unicode(35), server_default=text('(NULL)'))
    last_education = Column(Unicode(50), server_default=text('(NULL)'))
    last_employment = Column(Unicode(50), server_default=text('(NULL)'))

    address = relationship('MtrAddress', back_populates='mtr_user_details')
    mtr_city = relationship('MtrCity', back_populates='mtr_user_details')
    company = relationship('MtrCompany', back_populates='mtr_user_details')
    cost_center = relationship('MtrCostCenter', back_populates='mtr_user_details')
    division = relationship('MtrDivision', back_populates='mtr_user_details')
    job_position = relationship('MtrJobPosition', back_populates='mtr_user_details')
    job_title = relationship('MtrJobTitle', back_populates='mtr_user_details')
    profit_center = relationship('MtrProfitCenter', back_populates='mtr_user_details')
    skill_level = relationship('MtrSkillLevel', back_populates='mtr_user_details')
    user = relationship('UserLogin', back_populates='mtr_user_details')
    mtr_employee_group = relationship('MtrEmployeeGroup', back_populates='employee')
    mtr_source_document = relationship('MtrSourceDocument', foreign_keys=['MtrSourceDocument.signature_employee_1'], back_populates='mtr_user_details')
    mtr_source_document_ = relationship('MtrSourceDocument', foreign_keys=['MtrSourceDocument.signature_employee_2'], back_populates='mtr_user_details_')
    mtr_source_document1 = relationship('MtrSourceDocument', foreign_keys=['MtrSourceDocument.signature_employee_3'], back_populates='mtr_user_details1')
    mtr_source_document2 = relationship('MtrSourceDocument', foreign_keys=['MtrSourceDocument.signature_employee_4'], back_populates='mtr_user_details2')


class MtrBankCompany(Base):
    __tablename__ = 'mtr_bank_company'
    __table_args__ = {'schema': 'finance'}

    bank_company_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    company_id = Column(ForeignKey('general.mtr_company.company_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    bank_company_code = Column(Unicode(10), nullable=False, unique=True)
    bank_company_description = Column(Unicode(50), nullable=False)
    bank_id = Column(ForeignKey('finance.mtr_bank.bank_id'), nullable=False)
    bank_branch_id = Column(ForeignKey('finance.mtr_bank_branch.bank_branch_id'), nullable=False)
    bank_company_account_no = Column(Unicode(50), nullable=False)
    bank_company_account_name = Column(Unicode(60), nullable=False)
    account_type_id = Column(ForeignKey('common.mtr_bank_account_type.bank_account_type_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    currency_id = Column(ForeignKey('finance.mtr_currency.currency_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    bank_company_balance_limit = Column(Numeric(17, 4), nullable=False)
    bank_company_payment_limit = Column(Numeric(17, 4), nullable=False)
    brand_id = Column(ForeignKey('sales.mtr_brand.brand_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    profit_center_business_category_id = Column(ForeignKey('finance.mtr_profit_center_business_category.profit_center_business_category_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    cost_center_id = Column(ForeignKey('general.mtr_cost_center.cost_center_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    is_active = Column(Boolean, server_default=text('((1))'))
    bank_account_type = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    bank_company_receive = Column(Boolean, server_default=text('((0))'))
    bank_company_disbursement = Column(Boolean, server_default=text('((0))'))
    bank_company_allow_overdraft = Column(Boolean, server_default=text('((0))'))
    daily_rpt_code = Column(Unicode(50))
    vat_map = Column(Unicode(3))
    qris_mpan = Column(Unicode(35))

    account_type = relationship('MtrBankAccountType', back_populates='mtr_bank_company')
    bank_branch = relationship('MtrBankBranch', back_populates='mtr_bank_company')
    bank = relationship('MtrBank', back_populates='mtr_bank_company')
    brand = relationship('MtrBrand', back_populates='mtr_bank_company')
    company = relationship('MtrCompany', back_populates='mtr_bank_company')
    cost_center = relationship('MtrCostCenter', back_populates='mtr_bank_company')
    currency = relationship('MtrCurrency', back_populates='mtr_bank_company')
    profit_center_business_category = relationship('MtrProfitCenterBusinessCategory', back_populates='mtr_bank_company')
    mtr_customer_va_dbs = relationship('MtrCustomerVaDbs', back_populates='bank_company')
    mtr_reference = relationship('MtrReference', back_populates='bank_acc_receive_company')
    mtr_source_document = relationship('MtrSourceDocument', back_populates='bank_company')
    mtr_source_document_detail = relationship('MtrSourceDocumentDetail', back_populates='bank_company')


class MtrEmployeeGroup(Base):
    __tablename__ = 'mtr_employee_group'
    __table_args__ = {'schema': 'general'}

    employee_group_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    company_id = Column(ForeignKey('general.mtr_company.company_id'), nullable=False)
    employee_id = Column(ForeignKey('general.mtr_user_details.user_employee_id'), nullable=False)
    employee_group_code = Column(Unicode(10), unique=True)
    employee_group_name = Column(Unicode(100))
    is_active = Column(Boolean, server_default=text('((1))'))

    company = relationship('MtrCompany', back_populates='mtr_employee_group')
    employee = relationship('MtrUserDetails', back_populates='mtr_employee_group')
    mtr_employee_member = relationship('MtrEmployeeMember', back_populates='employee_group')


class MtrSupplier(Base):
    __tablename__ = 'mtr_supplier'
    __table_args__ = {'schema': 'general'}

    supplier_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    supplier_code = Column(Unicode(20), nullable=False, unique=True, server_default=text("('')"))
    supplier_name = Column(Unicode(100), nullable=False, server_default=text("('')"))
    supplier_behaviour = Column(Unicode(5), nullable=False, server_default=text("('')"))
    term_of_payment_id = Column(ForeignKey('general.mtr_term_of_payment.term_of_payment_id'), nullable=False)
    minimum_down_payment = Column(Float(53), nullable=False)
    default_currency_id = Column(Integer, nullable=False)
    vat_transaction_code = Column(Unicode(10), nullable=False, server_default=text("('')"))
    tax_name = Column(Unicode(100), nullable=False, server_default=text("('')"))
    tax_pkp_no = Column(Unicode(30), nullable=False, server_default=text("('')"))
    supplier_type_id = Column(ForeignKey('general.mtr_supplier_type.supplier_type_id'))
    supplier_class = Column(Unicode(20), server_default=text("('')"))
    supplier_title_prefix = Column(Unicode(20), server_default=text("('')"))
    supplier_title_suffix = Column(Unicode(20), server_default=text("('')"))
    supplier_address_id = Column(ForeignKey('general.mtr_address.address_id'))
    supplier_phone_no = Column(Unicode(30), server_default=text("('')"))
    supplier_fax_no = Column(Unicode(30), server_default=text("('')"))
    supplier_mobile_phone = Column(Unicode(30), server_default=text("('')"))
    supplier_email_address = Column(Unicode(128), server_default=text("('')"))
    supplier_invoice_type = Column(Unicode(10))
    via_binning = Column(Boolean)
    old_supplier_code = Column(Unicode(20))
    business_group_id = Column(Integer)
    supplier_unique_id = Column(Unicode(50))
    effective_date = Column(DateTime)
    is_import_supplier = Column(Boolean)
    vat_npwp_no = Column(Unicode(30), server_default=text("('')"))
    vat_npwp_date = Column(DateTime)
    vat_name = Column(Unicode(100), server_default=text("('')"))
    vat_address_id = Column(ForeignKey('general.mtr_address.address_id'))
    vat_pkp_type = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    vat_pkp_no = Column(Unicode(30), server_default=text("('')"))
    vat_kpp_id = Column(ForeignKey('general.mtr_kpp.kpp_id'))
    tax_npwp_no = Column(Unicode(30), server_default=text("('')"))
    tax_address_id = Column(ForeignKey('general.mtr_address.address_id'))
    tax_pkp_status = Column(Boolean, server_default=text('((0))'))
    tax_pkp_date = Column(DateTime)
    tax_pkp_type = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    tax_kpp_id = Column(ForeignKey('general.mtr_kpp.kpp_id'))
    vat_pkp_date = Column(DateTime)
    tax_npwp_date = Column(DateTime)

    supplier_address = relationship('MtrAddress', foreign_keys=[supplier_address_id], back_populates='mtr_supplier')
    supplier_type = relationship('MtrSupplierType', back_populates='mtr_supplier')
    tax_address = relationship('MtrAddress', foreign_keys=[tax_address_id], back_populates='mtr_supplier_')
    tax_kpp = relationship('MtrKpp', foreign_keys=[tax_kpp_id], back_populates='mtr_supplier')
    term_of_payment = relationship('MtrTermOfPayment', back_populates='mtr_supplier')
    vat_address = relationship('MtrAddress', foreign_keys=[vat_address_id], back_populates='mtr_supplier1')
    vat_kpp = relationship('MtrKpp', foreign_keys=[vat_kpp_id], back_populates='mtr_supplier_')
    mtr_leasing_document = relationship('MtrLeasingDocument', back_populates='supplier')
    mtr_supplier_bank_account = relationship('MtrSupplierBankAccount', back_populates='supplier')
    mtr_supplier_pic = relationship('MtrSupplierPic', back_populates='supplier')
    mtr_supplier_price_list = relationship('MtrSupplierPriceList', back_populates='supplier')


class MtrSupplierReference(Base):
    __tablename__ = 'mtr_supplier_reference'
    __table_args__ = {'schema': 'general'}

    supplier_status = Column(CHAR(2, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    supplier_reference_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    supplier_name = Column(Unicode(100), nullable=False)
    supplier_class = Column(Unicode(10), nullable=False)
    supplier_behaviour = Column(Unicode(5), nullable=False)
    term_of_payment_id = Column(ForeignKey('general.mtr_term_of_payment.term_of_payment_id'), nullable=False)
    vat_transaction_code = Column(Unicode(10), nullable=False, server_default=text("('')"))
    tax_name = Column(Unicode(100), nullable=False, server_default=text("('')"))
    tax_pkp_no = Column(Unicode(30), nullable=False, server_default=text("('')"))
    supplier_code = Column(Unicode(10))
    supplier_type_id = Column(ForeignKey('general.mtr_supplier_type.supplier_type_id'))
    supplier_title_prefix = Column(Unicode(15))
    supplier_title_suffix = Column(Unicode(15))
    supplier_address_id = Column(ForeignKey('general.mtr_address.address_id'))
    supplier_phone_no = Column(Unicode(30))
    supplier_fax_no = Column(Unicode(30))
    supplier_mobile_phone = Column(Unicode(30))
    supplier_email_address = Column(Unicode(128))
    minimum_down_payment = Column(Float(53))
    via_binning = Column(Boolean)
    old_supplier_code = Column(Unicode(10))
    business_group_id = Column(Integer)
    supplier_unique_id = Column(Unicode(50))
    company_id = Column(ForeignKey('general.mtr_company.company_id'))
    vat_npwp_no = Column(Unicode(30), server_default=text("('')"))
    vat_npwp_date = Column(DateTime)
    vat_name = Column(Unicode(100), server_default=text("('')"))
    vat_address_id = Column(ForeignKey('general.mtr_address.address_id'))
    vat_pkp_type = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    vat_pkp_no = Column(Unicode(30), server_default=text("('')"))
    vat_kpp_id = Column(ForeignKey('general.mtr_kpp.kpp_id'))
    tax_npwp_no = Column(Unicode(30), server_default=text("('')"))
    tax_address_id = Column(ForeignKey('general.mtr_address.address_id'))
    tax_pkp_status = Column(Boolean, server_default=text('((0))'))
    tax_pkp_date = Column(DateTime)
    tax_pkp_type = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    tax_kpp_id = Column(ForeignKey('general.mtr_kpp.kpp_id'))
    vat_pkp_date = Column(DateTime)
    tax_npwp_date = Column(DateTime)

    company = relationship('MtrCompany', back_populates='mtr_supplier_reference')
    supplier_address = relationship('MtrAddress', foreign_keys=[supplier_address_id], back_populates='mtr_supplier_reference')
    supplier_type = relationship('MtrSupplierType', back_populates='mtr_supplier_reference')
    tax_address = relationship('MtrAddress', foreign_keys=[tax_address_id], back_populates='mtr_supplier_reference_')
    tax_kpp = relationship('MtrKpp', foreign_keys=[tax_kpp_id], back_populates='mtr_supplier_reference')
    term_of_payment = relationship('MtrTermOfPayment', back_populates='mtr_supplier_reference')
    vat_address = relationship('MtrAddress', foreign_keys=[vat_address_id], back_populates='mtr_supplier_reference1')
    vat_kpp = relationship('MtrKpp', foreign_keys=[vat_kpp_id], back_populates='mtr_supplier_reference_')
    mtr_supplier_reference_bank_account = relationship('MtrSupplierReferenceBankAccount', back_populates='supplier_reference')
    mtr_supplier_reference_pic = relationship('MtrSupplierReferencePic', back_populates='supplier_reference')


class MtrCustomerVaDbs(Base):
    __tablename__ = 'mtr_customer_va_dbs'
    __table_args__ = {'schema': 'general'}

    customer_va_dbs_id = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    customer_id = Column(Unicode(25))
    company_id = Column(ForeignKey('general.mtr_company.company_id', ondelete='CASCADE', onupdate='CASCADE'))
    bank_company_id = Column(ForeignKey('finance.mtr_bank_company.bank_company_id'))
    customer_va_dbs = Column(Unicode(20))
    approval_dbs = Column(Unicode(2))
    respons_dbs = Column(Unicode(512))
    cpc_code = Column(Unicode(5))

    bank_company = relationship('MtrBankCompany', back_populates='mtr_customer_va_dbs')
    company = relationship('MtrCompany', back_populates='mtr_customer_va_dbs')


class MtrEmployeeMember(MtrUserDetails):
    __tablename__ = 'mtr_employee_member'
    __table_args__ = {'schema': 'general'}

    employee_member_id = Column(ForeignKey('general.mtr_user_details.user_employee_id'), Identity(start=1, increment=1), primary_key=True)
    company_id = Column(Integer, nullable=False)
    employee_group_id = Column(ForeignKey('general.mtr_employee_group.employee_group_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    employee_member_code = Column(Unicode(5))
    is_active = Column(Boolean, server_default=text('((1))'))

    employee_group = relationship('MtrEmployeeGroup', back_populates='mtr_employee_member')


class MtrLeasingDocument(Base):
    __tablename__ = 'mtr_leasing_document'
    __table_args__ = {'schema': 'general'}

    leasing_document_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    supplier_id = Column(ForeignKey('general.mtr_supplier.supplier_id'), nullable=False)
    is_active = Column(Boolean, server_default=text('((1))'))
    leasing_document_code = Column(Unicode(2), server_default=text("('')"))
    leasing_document_name = Column(Unicode(256), server_default=text("('')"))

    supplier = relationship('MtrSupplier', back_populates='mtr_leasing_document')


class MtrReference(Base):
    __tablename__ = 'mtr_reference'
    __table_args__ = {'schema': 'general'}

    reference_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    company_id = Column(ForeignKey('general.mtr_company.company_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    currency_id = Column(ForeignKey('finance.mtr_currency.currency_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    bank_acc_receive_company_id = Column(ForeignKey('finance.mtr_bank_company.bank_company_id'), nullable=False)
    item_broken_warehouse_id = Column(ForeignKey('aftersales.mtr_warehouse.warehouse_id'), nullable=False)
    unit_warehouse_id = Column(ForeignKey('aftersales.mtr_warehouse.warehouse_id'), nullable=False)
    margin_outer_kpp = Column(Numeric(5, 2))
    adjustment_reason_id = Column(ForeignKey('common.mtr_adjustment_reason.adjustment_reason_id', ondelete='CASCADE', onupdate='CASCADE'))
    lead_time_unit_etd = Column(Integer)
    vat_code = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    use_dms = Column(Boolean, server_default=text('((0))'))
    time_difference = Column(Numeric(2, 0), server_default=text('((0))'))
    operation_discount_outer_kpp = Column(Numeric(5, 2))
    check_month_end = Column(Boolean, server_default=text('((0))'))
    coa_group_id = Column(ForeignKey('finance.mtr_coa_group.coa_group_id', ondelete='CASCADE', onupdate='CASCADE'))
    with_vat = Column(Boolean, server_default=text('((0))'))
    approval_spm_id = Column(ForeignKey('common.mtr_approval_spm.approval_spm_id', ondelete='CASCADE', onupdate='CASCADE'))
    is_use_tax_industry = Column(Boolean)
    markup_percentage = Column(Numeric(5, 2))
    is_external_pdi = Column(Boolean)
    hide_cost = Column(Boolean)
    use_price_code = Column(Boolean)
    disable_edit_draft_soinvoice = Column(Boolean)

    adjustment_reason = relationship('MtrAdjustmentReason', back_populates='mtr_reference')
    approval_spm = relationship('MtrApprovalSpm', back_populates='mtr_reference')
    bank_acc_receive_company = relationship('MtrBankCompany', back_populates='mtr_reference')
    coa_group = relationship('MtrCoaGroup', back_populates='mtr_reference')
    company = relationship('MtrCompany', back_populates='mtr_reference')
    currency = relationship('MtrCurrency', back_populates='mtr_reference')
    item_broken_warehouse = relationship('MtrWarehouse', foreign_keys=[item_broken_warehouse_id], back_populates='mtr_reference')
    unit_warehouse = relationship('MtrWarehouse', foreign_keys=[unit_warehouse_id], back_populates='mtr_reference_')


class MtrSourceDocument(Base):
    __tablename__ = 'mtr_source_document'
    __table_args__ = (
        Index('mtr_source_document_UN', 'source_approval_document_id', 'brand_id', 'profit_center_id', 'transaction_type_id', 'bank_company_id', 'signature_employee_1', 'signature_employee_2', 'signature_employee_3', 'signature_employee_4', unique=True),
        {'schema': 'general'}
    )

    source_document_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    source_approval_document_id = Column(ForeignKey('common.mtr_source_approval_document.source_approval_document_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    brand_id = Column(ForeignKey('sales.mtr_brand.brand_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    profit_center_id = Column(ForeignKey('general.mtr_profit_center.profit_center_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    transaction_type_id = Column(ForeignKey('common.mtr_transaction_type.transaction_type_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    bank_company_id = Column(ForeignKey('finance.mtr_bank_company.bank_company_id'), nullable=False)
    source_document_name = Column(Unicode(128), nullable=False)
    source_document_format = Column(Unicode(50), nullable=False)
    source_document_reference = Column(Boolean, nullable=False)
    signature_employee_1 = Column(ForeignKey('general.mtr_user_details.user_employee_id'), nullable=False)
    signature_title_1 = Column(Unicode(50), nullable=False)
    signature_employee_2 = Column(ForeignKey('general.mtr_user_details.user_employee_id'), nullable=False)
    signature_title_2 = Column(Unicode(50), nullable=False)
    signature_employee_3 = Column(ForeignKey('general.mtr_user_details.user_employee_id'), nullable=False)
    signature_title_3 = Column(Unicode(50), nullable=False)
    signature_employee_4 = Column(ForeignKey('general.mtr_user_details.user_employee_id'), nullable=False)
    signature_title_4 = Column(Unicode(50), nullable=False)
    source_document_auto_number = Column(Boolean, nullable=False)
    source_document_reset_num_every = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    is_active = Column(Boolean, nullable=False)
    source_document_source_doc_prefix = Column(Unicode(128))
    source_document_brand_prefix = Column(Unicode(128))
    source_document_profit_cost_center_prefix = Column(Unicode(128))
    source_document_transaction_type_prefix = Column(Unicode(128))
    source_document_bank_acc_prefix = Column(Unicode(128))

    bank_company = relationship('MtrBankCompany', back_populates='mtr_source_document')
    brand = relationship('MtrBrand', back_populates='mtr_source_document')
    profit_center = relationship('MtrProfitCenter', back_populates='mtr_source_document')
    mtr_user_details = relationship('MtrUserDetails', foreign_keys=[signature_employee_1], back_populates='mtr_source_document')
    mtr_user_details_ = relationship('MtrUserDetails', foreign_keys=[signature_employee_2], back_populates='mtr_source_document_')
    mtr_user_details1 = relationship('MtrUserDetails', foreign_keys=[signature_employee_3], back_populates='mtr_source_document1')
    mtr_user_details2 = relationship('MtrUserDetails', foreign_keys=[signature_employee_4], back_populates='mtr_source_document2')
    source_approval_document = relationship('MtrSourceApprovalDocument', back_populates='mtr_source_document')
    transaction_type = relationship('MtrTransactionType', back_populates='mtr_source_document')


class MtrSourceDocumentDetail(Base):
    __tablename__ = 'mtr_source_document_detail'
    __table_args__ = (
        Index('mtr_source_document_detail_UN', 'source_approval_document_id', 'brand_id', 'profit_center_id', 'transaction_type_id', 'bank_company_id', unique=True),
        {'schema': 'general'}
    )

    source_document_detail_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    source_approval_document_id = Column(ForeignKey('common.mtr_source_approval_document.source_approval_document_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    brand_id = Column(ForeignKey('sales.mtr_brand.brand_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    profit_center_id = Column(ForeignKey('general.mtr_profit_center.profit_center_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    transaction_type_id = Column(ForeignKey('common.mtr_transaction_type.transaction_type_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    period_year = Column(Unicode(4), nullable=False)
    period_month = Column(CHAR(2, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    bank_company_id = Column(ForeignKey('finance.mtr_bank_company.bank_company_id'), nullable=False)
    last_document_number = Column(Numeric(15, 0), nullable=False)
    is_active = Column(Boolean, nullable=False)
    company_id = Column(ForeignKey('general.mtr_company.company_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    bank_company = relationship('MtrBankCompany', back_populates='mtr_source_document_detail')
    brand = relationship('MtrBrand', back_populates='mtr_source_document_detail')
    company = relationship('MtrCompany', back_populates='mtr_source_document_detail')
    profit_center = relationship('MtrProfitCenter', back_populates='mtr_source_document_detail')
    source_approval_document = relationship('MtrSourceApprovalDocument', back_populates='mtr_source_document_detail')
    transaction_type = relationship('MtrTransactionType', back_populates='mtr_source_document_detail')


class MtrSupplierBankAccount(Base):
    __tablename__ = 'mtr_supplier_bank_account'
    __table_args__ = {'schema': 'general'}

    supplier_bank_account_id = Column(Integer, primary_key=True)
    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    bank_id = Column(Integer, nullable=False)
    acc_type_id = Column(Integer, nullable=False)
    acc_name = Column(Unicode(60), nullable=False, server_default=text("('')"))
    acc_no = Column(Unicode(20), nullable=False, server_default=text("('')"))
    currency_id = Column(Integer, nullable=False)
    supplier_id = Column(ForeignKey('general.mtr_supplier.supplier_id'), nullable=False)

    supplier = relationship('MtrSupplier', back_populates='mtr_supplier_bank_account')


class MtrSupplierPic(Base):
    __tablename__ = 'mtr_supplier_pic'
    __table_args__ = {'schema': 'general'}

    supplier_pic_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    pic_code = Column(String(5, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    pic_name = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    pic_division_id = Column(ForeignKey('general.mtr_division.division_id'), nullable=False)
    pic_mobile_phone = Column(String(30, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    supplier_id = Column(ForeignKey('general.mtr_supplier.supplier_id'), nullable=False)
    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    pic_position_id = Column(Integer)

    pic_division = relationship('MtrDivision', back_populates='mtr_supplier_pic')
    supplier = relationship('MtrSupplier', back_populates='mtr_supplier_pic')


class MtrSupplierPriceList(Base):
    __tablename__ = 'mtr_supplier_price_list'
    __table_args__ = {'schema': 'general'}

    supplier_price_list_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    supplier_id = Column(ForeignKey('general.mtr_supplier.supplier_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    item_id = Column(Integer, nullable=False)
    order_type = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    price_amount = Column(Float(53), nullable=False)
    effective_date = Column(DateTime, nullable=False)
    currency_id = Column(Integer)

    supplier = relationship('MtrSupplier', back_populates='mtr_supplier_price_list')


class MtrSupplierReferenceBankAccount(Base):
    __tablename__ = 'mtr_supplier_reference_bank_account'
    __table_args__ = {'schema': 'general'}

    supplier_reference_bank_account_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    bank_id = Column(Integer, nullable=False)
    acc_type_id = Column(Integer, nullable=False)
    acc_name = Column(Unicode(60), nullable=False, server_default=text("('')"))
    acc_no = Column(Unicode(20), nullable=False, server_default=text("('')"))
    currency_id = Column(Integer, nullable=False)
    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    supplier_reference_id = Column(ForeignKey('general.mtr_supplier_reference.supplier_reference_id'))

    supplier_reference = relationship('MtrSupplierReference', back_populates='mtr_supplier_reference_bank_account')


class MtrSupplierReferencePic(Base):
    __tablename__ = 'mtr_supplier_reference_pic'
    __table_args__ = {'schema': 'general'}

    supplier_reference_pic_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    pic_code = Column(String(5, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    pic_name = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    pic_mobile_phone = Column(String(30, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    supplier_reference_id = Column(ForeignKey('general.mtr_supplier_reference.supplier_reference_id'), nullable=False)
    pic_division_id = Column(ForeignKey('general.mtr_division.division_id'))
    pic_position_id = Column(Integer)

    pic_division = relationship('MtrDivision', back_populates='mtr_supplier_reference_pic')
    supplier_reference = relationship('MtrSupplierReference', back_populates='mtr_supplier_reference_pic')

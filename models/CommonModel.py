from sqlalchemy import Boolean, CHAR, Column, Identity, Integer, Table, String, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = Base.metadata

class MtrAdjustmentReason(Base):
    __tablename__ = 'mtr_adjustment_reason' 
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    adjustment_reason_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    adjustment_reason_code = Column(String(20), unique=True)
    adjustment_reason_name = Column(String(256))

class MtrAftersalesArea(Base):
    __tablename__ = 'mtr_aftersales_area'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    aftersales_area_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    aftersales_area_code = Column(String(20), nullable=False, unique=True)
    aftersales_area_name = Column(String(256))

class MtrApprovalCode(Base):
    __tablename__ = 'mtr_approval_code'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    approval_code_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    approval_code = Column(String(20), nullable=False, unique=True, default="")
    approval_code_name = Column(String(256))

class MtrApprovalSpm(Base):
    __tablename__ = 'mtr_approval_spm'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    approval_spm_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    approval_spm_code = Column(String(20), unique=True)
    approval_spm_name = Column(String(256))

class MtrBankAccountType(Base):
    __tablename__ = 'mtr_bank_account_type'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    bank_account_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    bank_account_type_code = Column(String(20), nullable=False)
    bank_account_type_name = Column(String(256))

class MtrBillAbleTo(Base):
    __tablename__ = 'mtr_bill_able_to'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    billable_to_id = Column(Integer, primary_key=True)
    billable_to_code = Column(String(10), nullable=False)
    billable_to_name = Column(String(50), nullable=False)

class MtrBrandType(Base):
    __tablename__ = 'mtr_brand_type'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    brand_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    brand_type_code = Column(String(20), nullable=False, unique=True)
    brand_type_name = Column(String(256), nullable=False)

class MtrBusinessCategory(Base):
    __tablename__ = 'mtr_business_category'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    business_category_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    business_category_code = Column(String(20), unique=True)
    business_category_name = Column(String(256))

class MtrBusinessGroup(Base):
    __tablename__ = 'mtr_business_group'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    business_group_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    group_code = Column(String(10), nullable=False)
    group_name = Column(String(50), nullable=False)

class MtrBusinessScope(Base):
    __tablename__ = 'mtr_business_scope'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    business_scope_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    business_scope_code = Column(String(20), unique=True)
    business_scope_name = Column(String(256))

class MtrBusinessType(Base):
    __tablename__ = 'mtr_business_type'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    business_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    business_type_code = Column(String(20), unique=True)
    business_type_name = Column(String(256))

t_mtr_customer_class = Table(
    'mtr_customer_class', metadata,
    Column('customer_class_id', Integer, Identity(start=1, increment=1), nullable=False),
    Column('is_active', Boolean, nullable=False, server_default=text('((1))')),
    Column('class_code', CHAR(3, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('class_description', String(20)),
    schema='common'
    )

class MtrCustomerTypeFlagList(Base):
    __tablename__ = 'mtr_customer_type_flag_list'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False)
    customer_type_flag_list_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    customer_type_flag_list_code = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    customer_type_flag_list_name = Column(String(20), nullable=False)

class MtrFinanceArea(Base):
    __tablename__ = 'mtr_finance_area'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    finance_area_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    finance_area_code = Column(String(20), nullable=False, unique=True)
    finance_area_name = Column(String(256))

class MtrGeneralLedgerAccType(Base):
    __tablename__ = 'mtr_general_ledger_acc_type'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    general_ledger_acc_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    general_ledger_acc_type_code = Column(String(20), nullable=False, unique=True)
    general_ledger_acc_type_name = Column(String(256))

class MtrGeneralLedgerDimType(Base):
    __tablename__ = 'mtr_general_ledger_dim_type'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    general_ledger_dim_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    general_ledger_dim_type_code = Column(String(20), nullable=False, unique=True)
    general_ledger_dim_type_name = Column(String(256))

class MtrGeneralLedgerProcess(Base):
    __tablename__ = 'mtr_general_ledger_process'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    general_ledger_process_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    general_ledger_process_code = Column(String(20), nullable=False)
    general_ledger_process_name = Column(String(256))

class MtrIncentiveLevel(Base):
    __tablename__ = 'mtr_incentive_level'
    __table_args__ = {'schema': 'common'}

    incentive_level_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    incentive_level_variable = Column(String(50))
    incentive_level_code = Column(String(100))
    incentive_level_name = Column(String(50))

class MtrItemGroup(Base):
    __tablename__ = 'mtr_item_group'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False)
    item_group_id = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    item_group_code = Column(String(5), unique=True)
    item_group_name = Column(String(100))

class MtrJobPosition(Base):
    __tablename__ = 'mtr_job_position'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    job_position_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    job_position_code = Column(String(10), nullable=False, unique=True)
    job_position_name = Column(String(256), nullable=False)

class MtrJobTitle(Base):
    __tablename__ = 'mtr_job_title'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False)
    job_title_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    job_title_code = Column(String(5), nullable=False, unique=True)
    job_title_name = Column(String(100), nullable=False)

class MtrLineType(Base):
    __tablename__ = 'mtr_line_type'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False)
    line_type_id = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    line_type_code = Column(String(5), unique=True)
    line_type_name = Column(String(100))

class MtrPriceListCode(Base):
    __tablename__ = 'mtr_price_list_code'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    price_list_id = Column(Integer, nullable=False)
    price_list_code = Column(String(20), primary_key=True)
    price_list_code_name = Column(String(256), nullable=False)

class MtrReferenceTypePr(Base):
    __tablename__ = 'mtr_reference_type_pr'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    reference_type_id = Column(Integer, primary_key=True)
    reference_type_code = Column(String(5), nullable=False)
    reference_type_name = Column(String(100))

class MtrSalesGrade(Base):
    __tablename__ = 'mtr_sales_grade'
    __table_args__ = {'schema': 'common'}

    sales_grade_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    sales_grade_code = Column(String(10))
    sales_grade_name = Column(String(50))

class MtrSkillLevel(Base):
    __tablename__ = 'mtr_skill_level'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    skill_level_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    skill_level_code = Column(String(1), nullable=False, unique=True)

class MtrSkillLevelCode(Base):
    __tablename__ = 'mtr_skill_level_code'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    skill_level_code_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    skill_level_code = Column(String(5), nullable=False)

class MtrSourceApprovalDocument(Base):
    __tablename__ = 'mtr_source_approval_document'
    __table_args__ = {'schema': 'common'}

    source_approval_document_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    source_approval_document_code = Column(String(20), nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False)
    source_approval_document_name = Column(String(256))

class MtrSpecialMovement(Base):
    __tablename__ = 'mtr_special_movement'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    special_movement_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    special_movement_code = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, unique=True)
    special_movement_name = Column(String(100), nullable=False)

class MtrSubstituteType(Base):
    __tablename__ = 'mtr_substitute_type'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False)
    substitute_type_code = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    substitute_type_name = Column(String(50), nullable=False)

class MtrTaxFormatType(Base):
    __tablename__ = 'mtr_tax_format_type'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    tax_format_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    tax_format_type_code = Column(String(20), nullable=False, unique=True)
    tax_format_type_name = Column(String(256))

class MtrTaxOutTransaction(Base):
    __tablename__ = 'mtr_tax_out_transaction'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    tax_out_transaction_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    tax_out_transaction_code = Column(String(20), nullable=False, unique=True)
    tax_out_transaction_name = Column(String(256))

class MtrTransactionType(Base):
    __tablename__ = 'mtr_transaction_type'
    __table_args__ = {'schema': 'common'}

    transaction_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    transaction_type_code = Column(String(20), nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False)
    transaction_type_name = Column(String(256))

class MtrTransactionTypeCashManagementOut(Base):
    __tablename__ = 'mtr_transaction_type_cash_management_out'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    transaction_type_cash_management_out_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    transaction_type_cash_management_out_code = Column(String(20), nullable=False)
    transaction_type_cash_management_out_name = Column(String(256))

class MtrUomItem(Base):
    __tablename__ = 'mtr_uom_item'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    uom_item_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    uom_item_code = Column(String(10), nullable=False, unique=True)
    uom_item_name = Column(String(50), nullable=False)

class MtrVoidTransaction(Base):
    __tablename__ = 'mtr_void_transaction'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    void_transaction_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    void_transaction_code = Column(String(20), nullable=False, unique=True)
    void_transaction_name = Column(String(256))

class MtrWorkorderTransactionType(Base):
    __tablename__ = 'mtr_workorder_transaction_type'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    workorder_transaction_type_id = Column(Integer, primary_key=True)
    workorder_transaction_type_code = Column(String(20), nullable=False)
    workorder_transaction_type_name = Column(String(256), nullable=False)

class MtrWorkorderType(Base):
    __tablename__ = 'mtr_workorder_type'
    __table_args__ = {'schema': 'common'}

    is_active = Column(Boolean, nullable=False, server_default=text('((1))'))
    workorder_type_id = Column(Integer, primary_key=True)
    workorder_type_code = Column(String(10), nullable=False)
    workorder_type_name = Column(String(50), nullable=False)
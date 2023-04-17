from sqlalchemy.orm import Session
from models import GeneralLedgerAccountTypeModel

def get_general_ledger_account_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(GeneralLedgerAccountTypeModel.MtrGeneralLedgerAccountType).order_by(GeneralLedgerAccountTypeModel.MtrGeneralLedgerAccountType.general_ledger_account_type_id).offset(offset).limit(limit).all()


def get_general_ledger_account_type_cruds(db:Session,get_id:int):
    return  db.query(GeneralLedgerAccountTypeModel.MtrGeneralLedgerAccountType).filter(GeneralLedgerAccountTypeModel.MtrGeneralLedgerAccountType.general_ledger_account_type_id==get_id).first()
    

def post_general_ledger_account_type_cruds(db:Session, payload:GeneralLedgerAccountTypeModel.MtrGeneralLedgerAccountType):
    return GeneralLedgerAccountTypeModel.MtrGeneralLedgerAccountType(**payload.dict())

def delete_general_ledger_account_type_cruds(db:Session,get_id:int):
    return db.query(GeneralLedgerAccountTypeModel.MtrGeneralLedgerAccountType).filter(GeneralLedgerAccountTypeModel.MtrGeneralLedgerAccountType.general_ledger_account_type_id==get_id).delete(synchronize_session=False)
    
def put_general_ledger_account_type_cruds(db:Session,payload:GeneralLedgerAccountTypeModel.MtrGeneralLedgerAccountType, get_id:int):
    edit_general_ledger_account_type = db.query(GeneralLedgerAccountTypeModel.MtrGeneralLedgerAccountType).filter(GeneralLedgerAccountTypeModel.MtrGeneralLedgerAccountType.general_ledger_account_type_id==get_id)
    edit_general_ledger_account_type.update(payload.dict())
    messages_general_ledger_account_type = edit_general_ledger_account_type.first()
    return edit_general_ledger_account_type, messages_general_ledger_account_type

def patch_general_ledger_account_type_cruds(db:Session, get_id:int):
    return db.query(GeneralLedgerAccountTypeModel.MtrGeneralLedgerAccountType).filter(GeneralLedgerAccountTypeModel.MtrGeneralLedgerAccountType.general_ledger_account_type_id==get_id).first()

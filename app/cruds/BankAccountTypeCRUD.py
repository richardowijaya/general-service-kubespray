from sqlalchemy.orm import Session
from models import BankAccountTypeModel

def get_bank_account_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(BankAccountTypeModel.MtrBankAccountType).order_by(BankAccountTypeModel.MtrBankAccountType.bank_account_type_id).offset(offset).limit(limit).all()


def get_bank_account_type_cruds(db:Session,get_id:int):
    return  db.query(BankAccountTypeModel.MtrBankAccountType).filter(BankAccountTypeModel.MtrBankAccountType.bank_account_type_id==get_id).first()
    

def post_bank_account_type_cruds(db:Session, payload:BankAccountTypeModel.MtrBankAccountType):
    return BankAccountTypeModel.MtrBankAccountType(**payload.dict())

def delete_bank_account_type_cruds(db:Session,get_id:int):
    return db.query(BankAccountTypeModel.MtrBankAccountType).filter(BankAccountTypeModel.MtrBankAccountType.bank_account_type_id==get_id).delete(synchronize_session=False)
    
def put_bank_account_type_cruds(db:Session,payload:BankAccountTypeModel.MtrBankAccountType, get_id:int):
    edit_bank_account_type = db.query(BankAccountTypeModel.MtrBankAccountType).filter(BankAccountTypeModel.MtrBankAccountType.bank_account_type_id==get_id)
    edit_bank_account_type.update(payload.dict())
    messages_bank_account_type = edit_bank_account_type.first()
    return edit_bank_account_type, messages_bank_account_type

def patch_bank_account_type_cruds(db:Session, get_id:int):
    return db.query(BankAccountTypeModel.MtrBankAccountType).filter(BankAccountTypeModel.MtrBankAccountType.bank_account_type_id==get_id).first()

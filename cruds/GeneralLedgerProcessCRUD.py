from sqlalchemy.orm import Session
from models import GeneralLedgerProcessModel

def get_general_ledger_processs_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(GeneralLedgerProcessModel.MtrGeneralLedgerProcess).order_by(GeneralLedgerProcessModel.MtrGeneralLedgerProcess.general_ledger_process_id).offset(offset).limit(limit).all()


def get_general_ledger_process_cruds(db:Session,get_id:int):
    return  db.query(GeneralLedgerProcessModel.MtrGeneralLedgerProcess).filter(GeneralLedgerProcessModel.MtrGeneralLedgerProcess.general_ledger_process_id==get_id).first()
    

def post_general_ledger_process_cruds(db:Session, payload:GeneralLedgerProcessModel.MtrGeneralLedgerProcess):
    return GeneralLedgerProcessModel.MtrGeneralLedgerProcess(**payload.dict())

def delete_general_ledger_process_cruds(db:Session,get_id:int):
    return db.query(GeneralLedgerProcessModel.MtrGeneralLedgerProcess).filter(GeneralLedgerProcessModel.MtrGeneralLedgerProcess.general_ledger_process_id==get_id).delete(synchronize_session=False)
    
def put_general_ledger_process_cruds(db:Session,payload:GeneralLedgerProcessModel.MtrGeneralLedgerProcess, get_id:int):
    edit_general_ledger_process = db.query(GeneralLedgerProcessModel.MtrGeneralLedgerProcess).filter(GeneralLedgerProcessModel.MtrGeneralLedgerProcess.general_ledger_process_id==get_id)
    edit_general_ledger_process.update(payload.dict())
    messages_general_ledger_process = edit_general_ledger_process.first()
    return edit_general_ledger_process, messages_general_ledger_process

def patch_general_ledger_process_cruds(db:Session, get_id:int):
    return db.query(GeneralLedgerProcessModel.MtrGeneralLedgerProcess).filter(GeneralLedgerProcessModel.MtrGeneralLedgerProcess.general_ledger_process_id==get_id).first()

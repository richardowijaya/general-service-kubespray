from sqlalchemy.orm import Session
from models import TransactionTypeCashManagementOutModel

def get_transaction_type_cash_management_outs_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(TransactionTypeCashManagementOutModel.MtrTransactionTypeCashManagementOut).order_by(TransactionTypeCashManagementOutModel.MtrTransactionTypeCashManagementOut.transaction_type_cash_management_out_id).offset(offset).limit(limit).all()


def get_transaction_type_cash_management_out_cruds(db:Session,get_id:int):
    return  db.query(TransactionTypeCashManagementOutModel.MtrTransactionTypeCashManagementOut).filter(TransactionTypeCashManagementOutModel.MtrTransactionTypeCashManagementOut.transaction_type_cash_management_out_id==get_id).first()
    

def post_transaction_type_cash_management_out_cruds(db:Session, payload:TransactionTypeCashManagementOutModel.MtrTransactionTypeCashManagementOut):
    return TransactionTypeCashManagementOutModel.MtrTransactionTypeCashManagementOut(**payload.dict())

def delete_transaction_type_cash_management_out_cruds(db:Session,get_id:int):
    return db.query(TransactionTypeCashManagementOutModel.MtrTransactionTypeCashManagementOut).filter(TransactionTypeCashManagementOutModel.MtrTransactionTypeCashManagementOut.transaction_type_cash_management_out_id==get_id).delete(synchronize_session=False)
    
def put_transaction_type_cash_management_out_cruds(db:Session,payload:TransactionTypeCashManagementOutModel.MtrTransactionTypeCashManagementOut, get_id:int):
    edit_transaction_type_cash_management_out = db.query(TransactionTypeCashManagementOutModel.MtrTransactionTypeCashManagementOut).filter(TransactionTypeCashManagementOutModel.MtrTransactionTypeCashManagementOut.transaction_type_cash_management_out_id==get_id)
    edit_transaction_type_cash_management_out.update(payload.dict())
    messages_transaction_type_cash_management_out = edit_transaction_type_cash_management_out.first()
    return edit_transaction_type_cash_management_out, messages_transaction_type_cash_management_out

def patch_transaction_type_cash_management_out_cruds(db:Session, get_id:int):
    return db.query(TransactionTypeCashManagementOutModel.MtrTransactionTypeCashManagementOut).filter(TransactionTypeCashManagementOutModel.MtrTransactionTypeCashManagementOut.transaction_type_cash_management_out_id==get_id).first()

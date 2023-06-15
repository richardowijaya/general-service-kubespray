from sqlalchemy.orm import Session
from models import VoidTransactionModel

def get_void_transactions_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(VoidTransactionModel.MtrVoidTransaction).order_by(VoidTransactionModel.MtrVoidTransaction.void_transaction_id).offset(offset).limit(limit).all()


def get_void_transaction_cruds(db:Session,get_id:int):
    return  db.query(VoidTransactionModel.MtrVoidTransaction).filter(VoidTransactionModel.MtrVoidTransaction.void_transaction_id==get_id).first()
    

def post_void_transaction_cruds(db:Session, payload:VoidTransactionModel.MtrVoidTransaction):
    return VoidTransactionModel.MtrVoidTransaction(**payload.dict())

def delete_void_transaction_cruds(db:Session,get_id:int):
    return db.query(VoidTransactionModel.MtrVoidTransaction).filter(VoidTransactionModel.MtrVoidTransaction.void_transaction_id==get_id).delete(synchronize_session=False)
    
def put_void_transaction_cruds(db:Session,payload:VoidTransactionModel.MtrVoidTransaction, get_id:int):
    edit_void_transaction = db.query(VoidTransactionModel.MtrVoidTransaction).filter(VoidTransactionModel.MtrVoidTransaction.void_transaction_id==get_id)
    edit_void_transaction.update(payload.dict())
    messages_void_transaction = edit_void_transaction.first()
    return edit_void_transaction, messages_void_transaction

def patch_void_transaction_cruds(db:Session, get_id:int):
    return db.query(VoidTransactionModel.MtrVoidTransaction).filter(VoidTransactionModel.MtrVoidTransaction.void_transaction_id==get_id).first()

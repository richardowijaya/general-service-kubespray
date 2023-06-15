from sqlalchemy.orm import Session
from models import TaxOutTransactionModel

def get_tax_out_transactions_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(TaxOutTransactionModel.MtrTaxOutTransaction).order_by(TaxOutTransactionModel.MtrTaxOutTransaction.tax_out_transaction_id).offset(offset).limit(limit).all()


def get_tax_out_transaction_cruds(db:Session,get_id:int):
    return  db.query(TaxOutTransactionModel.MtrTaxOutTransaction).filter(TaxOutTransactionModel.MtrTaxOutTransaction.tax_out_transaction_id==get_id).first()
    

def post_tax_out_transaction_cruds(db:Session, payload:TaxOutTransactionModel.MtrTaxOutTransaction):
    return TaxOutTransactionModel.MtrTaxOutTransaction(**payload.dict())

def delete_tax_out_transaction_cruds(db:Session,get_id:int):
    return db.query(TaxOutTransactionModel.MtrTaxOutTransaction).filter(TaxOutTransactionModel.MtrTaxOutTransaction.tax_out_transaction_id==get_id).delete(synchronize_session=False)
    
def put_tax_out_transaction_cruds(db:Session,payload:TaxOutTransactionModel.MtrTaxOutTransaction, get_id:int):
    edit_tax_out_transaction = db.query(TaxOutTransactionModel.MtrTaxOutTransaction).filter(TaxOutTransactionModel.MtrTaxOutTransaction.tax_out_transaction_id==get_id)
    edit_tax_out_transaction.update(payload.dict())
    messages_tax_out_transaction = edit_tax_out_transaction.first()
    return edit_tax_out_transaction, messages_tax_out_transaction

def patch_tax_out_transaction_cruds(db:Session, get_id:int):
    return db.query(TaxOutTransactionModel.MtrTaxOutTransaction).filter(TaxOutTransactionModel.MtrTaxOutTransaction.tax_out_transaction_id==get_id).first()

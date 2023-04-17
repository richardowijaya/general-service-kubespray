from fastapi import APIRouter,Depends,HTTPException,status
from cruds import TaxOutTransactionCRUD
from exceptions.RequestException import ResponseException
from schemas import TaxOutTransactionSchema
from sqlalchemy.orm import Session
from configs.database import get_db
from payloads import CommonResponse

router = APIRouter(tags=["Tax Out Transaction SPM"],prefix="/api/general")

@router.get("/get-tax-out-transactions", status_code=200)
def get_tax_out_transactions(db:Session=Depends(get_db)):
    tax_out_transactions = TaxOutTransactionCRUD.get_tax_out_transactions_cruds(db,0,100)
    if not tax_out_transactions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),tax_out_transactions)

@router.get("/get-tax-out-transaction/{tax_out_transaction_id}", status_code=200)
def get_tax_out_transaction(tax_out_transaction_id, db:Session=Depends(get_db)):
    tax_out_transaction = TaxOutTransactionCRUD.get_tax_out_transaction_cruds(db, tax_out_transaction_id)
    if not tax_out_transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),tax_out_transaction)

@router.post("/create-tax-out-transaction", status_code=201)
def post_tax_out_transaction(payload:TaxOutTransactionSchema.MtrTaxOutTransactionGetSchema,db:Session=Depends(get_db)):
    new_tax_out_transaction = TaxOutTransactionCRUD.post_tax_out_transaction_cruds(db, payload)
    db.add(new_tax_out_transaction)
    db.commit()
    db.refresh(new_tax_out_transaction)
    return CommonResponse.payload(ResponseException(201), new_tax_out_transaction)

@router.delete("/delete-tax-out-transaction/{tax_out_transaction_id}", status_code=202)
def delete_tax_out_transaction(tax_out_transaction_id, db:Session=Depends(get_db)):
    erase_tax_out_transaction = TaxOutTransactionCRUD.delete_tax_out_transaction_cruds(db,tax_out_transaction_id)
    if not erase_tax_out_transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_tax_out_transaction)

@router.put("/update-tax-out-transaction/{tax_out_transaction_id}", status_code=202)
def put_tax_out_transaction(payload:TaxOutTransactionSchema.MtrTaxOutTransactionGetSchema, tax_out_transaction_id,db:Session=Depends(get_db)):
    update_tax_out_transaction, update_data_new  = TaxOutTransactionCRUD.put_tax_out_transaction_cruds(db,payload, tax_out_transaction_id)
    if not update_tax_out_transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-tax-out-transaction/{tax_out_transaction_id}", status_code=202)
def patch_tax_out_transaction(tax_out_transaction_id,db:Session=Depends(get_db)):
    active_tax_out_transaction  = TaxOutTransactionCRUD.patch_tax_out_transaction_cruds(db, tax_out_transaction_id)
    if not active_tax_out_transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_tax_out_transaction.is_active = not active_tax_out_transaction.is_active
    db.commit()
    db.refresh(active_tax_out_transaction)
    return CommonResponse.payload(ResponseException(200), active_tax_out_transaction.is_active)
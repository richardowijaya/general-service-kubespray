from fastapi import APIRouter,Depends,HTTPException,status
from cruds import BillableToCRUD
from exceptions.RequestException import ResponseException
from schemas import BillableToSchema
from sqlalchemy.orm import Session
from configs.database import get_db
from payloads import CommonResponse

router = APIRouter(tags=["Billable To"],prefix="/api/general")

@router.get("/get-billable-tos", status_code=200)
def get_billables_to(db:Session=Depends(get_db)):
    billables_to = BillableToCRUD.get_billables_to_cruds(db,0,100)
    if not billables_to:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),billables_to)

@router.get("/get-billable-to/{billable_to_id}", status_code=200)
def get_billable_to(billable_to_id, db:Session=Depends(get_db)):
    billable_to = BillableToCRUD.get_billable_to_cruds(db, billable_to_id)
    if not billable_to:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),billable_to)

@router.post("/create-billable-to", status_code=201)
def post_billable_to(payload:BillableToSchema.MtrBillableToGetSchema,db:Session=Depends(get_db)):
    new_billable_to = BillableToCRUD.post_billable_to_cruds(db, payload)
    db.add(new_billable_to)
    db.commit()
    db.refresh(new_billable_to)
    return CommonResponse.payload(ResponseException(201), new_billable_to)

@router.delete("/delete-billable-to/{billable_to_id}", status_code=202)
def delete_billable_to(billable_to_id, db:Session=Depends(get_db)):
    erase_billable_to = BillableToCRUD.delete_billable_to_cruds(db,billable_to_id)
    if not erase_billable_to:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_billable_to)

@router.put("/update-billable-to/{billable_to_id}", status_code=202)
def put_billable_to(payload:BillableToSchema.MtrBillableToGetSchema, billable_to_id,db:Session=Depends(get_db)):
    update_billable_to, update_data_new  = BillableToCRUD.put_billable_to_cruds(db,payload, billable_to_id)
    if not update_billable_to:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-billable-to/{billable_to_id}", status_code=202)
def patch_billable_to(billable_to_id,db:Session=Depends(get_db)):
    active_billable_to  = BillableToCRUD.patch_billable_to_cruds(db, billable_to_id)
    if not active_billable_to:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_billable_to.is_active = not active_billable_to.is_active
    db.commit()
    db.refresh(active_billable_to)
    return CommonResponse.payload(ResponseException(200), active_billable_to.is_active)
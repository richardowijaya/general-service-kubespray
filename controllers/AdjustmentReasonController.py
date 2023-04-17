from fastapi import APIRouter,Depends,HTTPException,status
from payloads import CommonResponse
from exceptions.RequestException import ResponseException 
from cruds import AdjustmentReasonCRUD
from schemas import AdjustmentReasonSchema
from sqlalchemy.orm import Session
from configs.database import get_db

router = APIRouter(tags=["Adjustment Reason"],prefix="/api/general")

@router.get("/get-adjustment-reasons", status_code=status.HTTP_200_OK)
def get_adjustment_reasons(db:Session=Depends(get_db)):
    adjustment_reasons = AdjustmentReasonCRUD.get_adjustment_reasons_cruds(db,0,100)
    if not adjustment_reasons:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),adjustment_reasons)

@router.get("/get-adjustment-reason/{adjustment_reason_id}", status_code=status.HTTP_200_OK)
def get_adjustment_reason(adjustment_reason_id, db:Session=Depends(get_db)):
    adjustment_reason = AdjustmentReasonCRUD.get_adjustment_reason_cruds(db, adjustment_reason_id)
    if not adjustment_reason:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200), adjustment_reason)

@router.post("/create-adjustment-reason", status_code=status.HTTP_201_CREATED)
def post_adjustment_reason(payload:AdjustmentReasonSchema.MtrAdjustmentReasonGetSchema,db:Session=Depends(get_db)):
    new_adjustment_reason = AdjustmentReasonCRUD.post_adjustment_reasons_cruds(db, payload)
    db.add(new_adjustment_reason)
    db.commit()
    db.refresh(new_adjustment_reason)
    return CommonResponse.payload(ResponseException(201), new_adjustment_reason)

@router.delete("/delete-adjustment-reason/{adjustment_reason_id}", status_code=status.HTTP_202_ACCEPTED)
def delete_adjustment_reason(adjustment_reason_id, db:Session=Depends(get_db)):
    erase_adjustment_reason = AdjustmentReasonCRUD.delete_adjustment_reason_cruds(db,adjustment_reason_id)
    if not erase_adjustment_reason:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_adjustment_reason)

@router.put("/update-adjustment-reason/{adjustment_reason_id}", status_code=status.HTTP_202_ACCEPTED)
def put_adjustment_reason(payload:AdjustmentReasonSchema.MtrAdjustmentReasonGetSchema, adjustment_reason_id,db:Session=Depends(get_db)):
    update_adjustment_reason, update_data_new  = AdjustmentReasonCRUD.put_adjustment_reason_cruds(db,payload, adjustment_reason_id)
    if not update_adjustment_reason:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-adjustment-reason/{adjustment_reason_id}", status_code=status.HTTP_202_ACCEPTED)
def patch_adjustment_reason(adjustment_reason_id,db:Session=Depends(get_db)):
    active_adjustment_reason  = AdjustmentReasonCRUD.patch_adjustment_reason_cruds(db, adjustment_reason_id)
    if not active_adjustment_reason:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_adjustment_reason.is_active = not active_adjustment_reason.is_active
    db.commit()
    db.refresh(active_adjustment_reason)
    return CommonResponse.payload(ResponseException(200), active_adjustment_reason.is_active)

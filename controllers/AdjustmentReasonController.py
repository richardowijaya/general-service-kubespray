from fastapi import APIRouter,Depends,HTTPException,status
from cruds import AdjustmentReasonCRUD
from schemas import AdjustmentReasonSchema
from sqlalchemy.orm import Session
from configs.database import get_db

router = APIRouter(tags=["Adjustment Reason"],prefix="/api/general")

@router.get("/get-adjustment-reasons", status_code=200)
def get_adjustment_reasons(db:Session=Depends(get_db)):
    adjustment_reasons = AdjustmentReasonCRUD.get_adjustment_reasons_cruds(db,0,100)
    if not adjustment_reasons:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No data found")
    return AdjustmentReasonSchema.MtrAdjustmentReasonResponses(status_code=200,message="Success",data=adjustment_reasons)

@router.get("/get-adjustment-reason/{adjustment_reason_id}", status_code=200)
def get_adjustment_reason(adjustment_reason_id, db:Session=Depends(get_db)):
    adjustment_reason = AdjustmentReasonCRUD.get_adjustment_reason_cruds(db, adjustment_reason_id)
    if not adjustment_reason:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    return AdjustmentReasonSchema.MtrAdjustmentReasonResponse(status_code=200, message="Success", data=adjustment_reason)

@router.post("/create-adjustment-reason", status_code=201)
def post_adjustment_reason(payload:AdjustmentReasonSchema.MtrAdjustmentReasonGetSchema,db:Session=Depends(get_db)):
    new_adjustment_reason = AdjustmentReasonCRUD.post_adjustment_reasons_cruds(db, payload)
    db.add(new_adjustment_reason)
    db.commit()
    db.refresh(new_adjustment_reason)
    return AdjustmentReasonSchema.MtrAdjustmentReasonResponse(status_code=201, message="Success", data=new_adjustment_reason)

@router.delete("/delete-adjustment-reason/{adjustment_reason_id}", status_code=202)
def delete_adjustment_reason(adjustment_reason_id, db:Session=Depends(get_db)):
    erase_adjustment_reason = AdjustmentReasonCRUD.delete_adjustment_reason_cruds(db,adjustment_reason_id)
    if not erase_adjustment_reason:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    db.commit()
    return AdjustmentReasonSchema.MtrAdjustmentReasonResponse(status_code=200, message="Success", data=erase_adjustment_reason)

@router.put("/update-adjustment-reason/{adjustment_reason_id}", status_code=202)
def put_adjustment_reason(payload:AdjustmentReasonSchema.MtrAdjustmentReasonGetSchema, adjustment_reason_id,db:Session=Depends(get_db)):
    update_adjustment_reason, update_data_new  = AdjustmentReasonCRUD.put_adjustment_reason_cruds(db,payload, adjustment_reason_id)
    if not update_adjustment_reason:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    db.commit()
    db.refresh(update_data_new)
    return AdjustmentReasonSchema.MtrAdjustmentReasonResponse(status_code=200, message="Success", data=update_data_new)

@router.patch("/active-adjustment-reason/{adjustment_reason_id}", status_code=202)
def patch_adjustment_reason(adjustment_reason_id,db:Session=Depends(get_db)):
    active_adjustment_reason  = AdjustmentReasonCRUD.patch_adjustment_reason_cruds(db, adjustment_reason_id)
    if not active_adjustment_reason:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    active_adjustment_reason.is_active = not active_adjustment_reason.is_active
    db.commit()
    db.refresh(active_adjustment_reason)
    return AdjustmentReasonSchema.MtrAdjustmentReasonResponse(status_code=200, message="Success", data=active_adjustment_reason)
from fastapi import APIRouter,Depends,HTTPException,status
from cruds import ApprovalCodeCRUD
from schemas import ApprovalCodeSchema
from sqlalchemy.orm import Session
from configs.database import get_db
from payloads import GeneralResponse

router = APIRouter(tags=["Approval Code"],prefix="/api/general")

@router.get("/get-approval-codes", status_code=200)
def get_approval_codes(db:Session=Depends(get_db)):
    approval_codes = ApprovalCodeCRUD.get_approval_codes_cruds(db,0,100)
    if not approval_codes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No data found")
    return GeneralResponse.payloads(200,"Success",approval_codes)

@router.get("/get-approval-code/{approval_code_id}", status_code=200)
def get_approval_code(approval_code_id, db:Session=Depends(get_db)):
    approval_code = ApprovalCodeCRUD.get_approval_code_cruds(db, approval_code_id)
    if not approval_code:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    return GeneralResponse.payload(200,"Success",approval_code)

@router.post("/create-approval-code", status_code=201)
def post_approval_code(payload:ApprovalCodeSchema.MtrApprovalCodeGetSchema,db:Session=Depends(get_db)):
    new_approval_code = ApprovalCodeCRUD.post_approval_code_cruds(db, payload)
    db.add(new_approval_code)
    db.commit()
    db.refresh(new_approval_code)
    return GeneralResponse.payload(status_code=201, message="Success", data=new_approval_code)

@router.delete("/delete-approval-code/{approval_code_id}", status_code=202)
def delete_approval_code(approval_code_id, db:Session=Depends(get_db)):
    erase_approval_code = ApprovalCodeCRUD.delete_approval_code_cruds(db,approval_code_id)
    if not erase_approval_code:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    db.commit()
    return GeneralResponse.payload(202, "Success", erase_approval_code)

@router.put("/update-approval-code/{approval_code_id}", status_code=202)
def put_approval_code(payload:ApprovalCodeSchema.MtrApprovalCodeGetSchema, approval_code_id,db:Session=Depends(get_db)):
    update_approval_code, update_data_new  = ApprovalCodeCRUD.put_approval_code_cruds(db,payload, approval_code_id)
    if not update_approval_code:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    db.commit()
    db.refresh(update_data_new)
    return GeneralResponse.payload(200, "Success", update_data_new)

@router.patch("/active-approval-code/{approval_code_id}", status_code=202)
def patch_approval_code(approval_code_id,db:Session=Depends(get_db)):
    active_approval_code  = ApprovalCodeCRUD.patch_approval_code_cruds(db, approval_code_id)
    if not active_approval_code:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    active_approval_code.is_active = not active_approval_code.is_active
    db.commit()
    db.refresh(active_approval_code)
    return GeneralResponse.payload(200, "Success", active_approval_code)
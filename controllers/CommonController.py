from fastapi import APIRouter,Depends,HTTPException,status
from cruds import CommonCRUD
from models import CommonModel
from schemas import CommonSchema
from sqlalchemy.orm import Session
from configs.database import get_db

router = APIRouter(tags=["Common"],prefix="/api/general")

@router.get("/adjustment-reasons")
def get_adjustment_reasons(db:Session=Depends(get_db)):
    items = CommonCRUD.get_adjustment_reasons_cruds(db)
    if not items:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="data not found")
    return {
        "status" : "success",
        "results" : len(items),
        "data" : items
    }

@router.post("/adjustment-reason")
def post_adjustment_reason(payload:CommonSchema.MtrAdjustmentReasonSchema,db:Session=Depends(get_db)):
    new_data = CommonModel.MtrAdjustmentReason(**payload.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {
        "status" : "success",
        "new_adjustment_reasons" : new_data
    }

@router.get("/aftersales-areas")
def get_aftersales_areas(db:Session=Depends(get_db)):
    items = CommonCRUD.get_aftersales_area_cruds(db)
    if not items:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="data not found")
    return {
        "status" : "success",
        "results" : len(items),
        "data" : items
    }

@router.post("/aftersales-area")
def post_after_sales_area(payload:CommonSchema.MtrAftersalesAreaSchema,db:Session=Depends(get_db)):
    new_data = CommonModel.MtrAftersalesArea(**payload.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {
        "status" : "success",
        "new_adjustment_reasons" : new_data
    }
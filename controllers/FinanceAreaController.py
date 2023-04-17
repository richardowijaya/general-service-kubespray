from fastapi import APIRouter,Depends,HTTPException,status
from cruds import FinanceAreaCRUD
from exceptions.RequestException import ResponseException
from schemas import FinanceAreaSchema
from sqlalchemy.orm import Session
from configs.database import get_db
from payloads import CommonResponse

router = APIRouter(tags=["Finance Area"],prefix="/api/general")

@router.get("/get-finance-areas", status_code=200)
def get_finance_areas(db:Session=Depends(get_db)):
    finance_areas = FinanceAreaCRUD.get_finance_areas_cruds(db,0,100)
    if not finance_areas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),finance_areas)

@router.get("/get-finance-area/{finance_area_id}", status_code=200)
def get_finance_area(finance_area_id, db:Session=Depends(get_db)):
    finance_area = FinanceAreaCRUD.get_finance_area_cruds(db, finance_area_id)
    if not finance_area:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),finance_area)

@router.post("/create-finance-area", status_code=201)
def post_finance_area(payload:FinanceAreaSchema.MtrFinanceAreaGetSchema,db:Session=Depends(get_db)):
    new_finance_area = FinanceAreaCRUD.post_finance_area_cruds(db, payload)
    db.add(new_finance_area)
    db.commit()
    db.refresh(new_finance_area)
    return CommonResponse.payload(ResponseException(201), new_finance_area)

@router.delete("/delete-finance-area/{finance_area_id}", status_code=202)
def delete_finance_area(finance_area_id, db:Session=Depends(get_db)):
    erase_finance_area = FinanceAreaCRUD.delete_finance_area_cruds(db,finance_area_id)
    if not erase_finance_area:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_finance_area)

@router.put("/update-finance-area/{finance_area_id}", status_code=202)
def put_finance_area(payload:FinanceAreaSchema.MtrFinanceAreaGetSchema, finance_area_id,db:Session=Depends(get_db)):
    update_finance_area, update_data_new  = FinanceAreaCRUD.put_finance_area_cruds(db,payload, finance_area_id)
    if not update_finance_area:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-finance-area/{finance_area_id}", status_code=202)
def patch_finance_area(finance_area_id,db:Session=Depends(get_db)):
    active_finance_area  = FinanceAreaCRUD.patch_finance_area_cruds(db, finance_area_id)
    if not active_finance_area:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_finance_area.is_active = not active_finance_area.is_active
    db.commit()
    db.refresh(active_finance_area)
    return CommonResponse.payload(ResponseException(200), active_finance_area.is_active)
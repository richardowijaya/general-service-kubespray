from fastapi import APIRouter,Depends,HTTPException,status
from cruds import WorkOrderTypeCRUD
from exceptions.RequestException import ResponseException
from schemas import WorkOrderTypeSchema
from sqlalchemy.orm import Session
from configs.database import get_db
from payloads import CommonResponse

router = APIRouter(tags=["Work Order Type"],prefix="/api/general")

@router.get("/get-work-order-types", status_code=200)
def get_work_order_types(db:Session=Depends(get_db)):
    work_order_types = WorkOrderTypeCRUD.get_work_order_types_cruds(db,0,100)
    if not work_order_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),work_order_types)

@router.get("/get-work-order-type/{work_order_type_id}", status_code=200)
def get_work_order_type(work_order_type_id, db:Session=Depends(get_db)):
    work_order_type = WorkOrderTypeCRUD.get_work_order_type_cruds(db, work_order_type_id)
    if not work_order_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),work_order_type)

@router.post("/create-work-order-type", status_code=201)
def post_work_order_type(payload:WorkOrderTypeSchema.MtrWorkOrderTypeGetSchema,db:Session=Depends(get_db)):
    new_work_order_type = WorkOrderTypeCRUD.post_work_order_type_cruds(db, payload)
    db.add(new_work_order_type)
    db.commit()
    db.refresh(new_work_order_type)
    return CommonResponse.payload(ResponseException(201), new_work_order_type)

@router.delete("/delete-work-order-type/{work_order_type_id}", status_code=202)
def delete_work_order_type(work_order_type_id, db:Session=Depends(get_db)):
    erase_work_order_type = WorkOrderTypeCRUD.delete_work_order_type_cruds(db,work_order_type_id)
    if not erase_work_order_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_work_order_type)

@router.put("/update-work-order-type/{work_order_type_id}", status_code=202)
def put_work_order_type(payload:WorkOrderTypeSchema.MtrWorkOrderTypeGetSchema, work_order_type_id,db:Session=Depends(get_db)):
    update_work_order_type, update_data_new  = WorkOrderTypeCRUD.put_work_order_type_cruds(db,payload, work_order_type_id)
    if not update_work_order_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-work-order-type/{work_order_type_id}", status_code=202)
def patch_work_order_type(work_order_type_id,db:Session=Depends(get_db)):
    active_work_order_type  = WorkOrderTypeCRUD.patch_work_order_type_cruds(db, work_order_type_id)
    if not active_work_order_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_work_order_type.is_active = not active_work_order_type.is_active
    db.commit()
    db.refresh(active_work_order_type)
    return CommonResponse.payload(ResponseException(200), active_work_order_type.is_active)
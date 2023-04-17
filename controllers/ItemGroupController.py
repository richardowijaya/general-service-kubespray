from fastapi import APIRouter,Depends,HTTPException,status
from cruds import ItemGroupCRUD
from exceptions.RequestException import ResponseException
from schemas import ItemGroupSchema
from sqlalchemy.orm import Session
from configs.database import get_db
from payloads import CommonResponse

router = APIRouter(tags=["Item Group"],prefix="/api/general")

@router.get("/get-item-groups", status_code=200)
def get_item_groups(db:Session=Depends(get_db)):
    item_groups = ItemGroupCRUD.get_item_groups_cruds(db,0,100)
    if not item_groups:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),item_groups)

@router.get("/get-item-group/{item_group_id}", status_code=200)
def get_item_group(item_group_id, db:Session=Depends(get_db)):
    item_group = ItemGroupCRUD.get_item_group_cruds(db, item_group_id)
    if not item_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),item_group)

@router.post("/create-item-group", status_code=201)
def post_item_group(payload:ItemGroupSchema.MtrItemGroupGetSchema,db:Session=Depends(get_db)):
    new_item_group = ItemGroupCRUD.post_item_group_cruds(db, payload)
    db.add(new_item_group)
    db.commit()
    db.refresh(new_item_group)
    return CommonResponse.payload(ResponseException(201), new_item_group)

@router.delete("/delete-item-group/{item_group_id}", status_code=202)
def delete_item_group(item_group_id, db:Session=Depends(get_db)):
    erase_item_group = ItemGroupCRUD.delete_item_group_cruds(db,item_group_id)
    if not erase_item_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_item_group)

@router.put("/update-item-group/{item_group_id}", status_code=202)
def put_item_group(payload:ItemGroupSchema.MtrItemGroupGetSchema, item_group_id,db:Session=Depends(get_db)):
    update_item_group, update_data_new  = ItemGroupCRUD.put_item_group_cruds(db,payload, item_group_id)
    if not update_item_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-item-group/{item_group_id}", status_code=202)
def patch_item_group(item_group_id,db:Session=Depends(get_db)):
    active_item_group  = ItemGroupCRUD.patch_item_group_cruds(db, item_group_id)
    if not active_item_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_item_group.is_active = not active_item_group.is_active
    db.commit()
    db.refresh(active_item_group)
    return CommonResponse.payload(ResponseException(200), active_item_group.is_active)
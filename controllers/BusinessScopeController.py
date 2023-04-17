from fastapi import APIRouter,Depends,HTTPException,status
from cruds import BusinessScopeCRUD
from exceptions.RequestException import ResponseException
from schemas import BusinessScopeSchema
from sqlalchemy.orm import Session
from configs.database import get_db
from payloads import CommonResponse

router = APIRouter(tags=["Business Scope"],prefix="/api/general")

@router.get("/get-business-scopes", status_code=200)
def get_business_scopes(db:Session=Depends(get_db)):
    business_scopes = BusinessScopeCRUD.get_business_scopes_cruds(db,0,100)
    if not business_scopes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),business_scopes)

@router.get("/get-business-scope/{business_scope_id}", status_code=200)
def get_business_scope(business_scope_id, db:Session=Depends(get_db)):
    business_scope = BusinessScopeCRUD.get_business_scope_cruds(db, business_scope_id)
    if not business_scope:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),business_scope)

@router.post("/create-business-scope", status_code=201)
def post_business_scope(payload:BusinessScopeSchema.MtrBusinessScopeGetSchema,db:Session=Depends(get_db)):
    new_business_scope = BusinessScopeCRUD.post_business_scope_cruds(db, payload)
    db.add(new_business_scope)
    db.commit()
    db.refresh(new_business_scope)
    return CommonResponse.payload(ResponseException(201), new_business_scope)

@router.delete("/delete-business-scope/{business_scope_id}", status_code=202)
def delete_business_scope(business_scope_id, db:Session=Depends(get_db)):
    erase_business_scope = BusinessScopeCRUD.delete_business_scope_cruds(db,business_scope_id)
    if not erase_business_scope:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_business_scope)

@router.put("/update-business-scope/{business_scope_id}", status_code=202)
def put_business_scope(payload:BusinessScopeSchema.MtrBusinessScopeGetSchema, business_scope_id,db:Session=Depends(get_db)):
    update_business_scope, update_data_new  = BusinessScopeCRUD.put_business_scope_cruds(db,payload, business_scope_id)
    if not update_business_scope:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-business-scope/{business_scope_id}", status_code=202)
def patch_business_scope(business_scope_id,db:Session=Depends(get_db)):
    active_business_scope  = BusinessScopeCRUD.patch_business_scope_cruds(db, business_scope_id)
    if not active_business_scope:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_business_scope.is_active = not active_business_scope.is_active
    db.commit()
    db.refresh(active_business_scope)
    return CommonResponse.payload(ResponseException(200), active_business_scope.is_active)
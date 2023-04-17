from fastapi import APIRouter,Depends,HTTPException,status
from cruds import ReferenceTypePurchaseRequestCRUD
from exceptions.RequestException import ResponseException
from schemas import ReferenceTypePurchaseRequestSchema
from sqlalchemy.orm import Session
from configs.database import get_db
from payloads import CommonResponse

router = APIRouter(tags=["Reference Type Purchase Request"],prefix="/api/general")

@router.get("/get-reference-type-purchase-requests", status_code=200)
def get_reference_type_purchase_requests(db:Session=Depends(get_db)):
    reference_type_purchase_requests = ReferenceTypePurchaseRequestCRUD.get_reference_type_purchase_requests_cruds(db,0,100)
    if not reference_type_purchase_requests:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),reference_type_purchase_requests)

@router.get("/get-reference-type-purchase-request/{reference_type_purchase_request_id}", status_code=200)
def get_reference_type_purchase_request(reference_type_purchase_request_id, db:Session=Depends(get_db)):
    reference_type_purchase_request = ReferenceTypePurchaseRequestCRUD.get_reference_type_purchase_request_cruds(db, reference_type_purchase_request_id)
    if not reference_type_purchase_request:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),reference_type_purchase_request)

@router.post("/create-reference-type-purchase-request", status_code=201)
def post_reference_type_purchase_request(payload:ReferenceTypePurchaseRequestSchema.MtrReferenceTypePurchaseRequestGetSchema,db:Session=Depends(get_db)):
    new_reference_type_purchase_request = ReferenceTypePurchaseRequestCRUD.post_reference_type_purchase_request_cruds(db, payload)
    db.add(new_reference_type_purchase_request)
    db.commit()
    db.refresh(new_reference_type_purchase_request)
    return CommonResponse.payload(ResponseException(201), new_reference_type_purchase_request)

@router.delete("/delete-reference-type-purchase-request/{reference_type_purchase_request_id}", status_code=202)
def delete_reference_type_purchase_request(reference_type_purchase_request_id, db:Session=Depends(get_db)):
    erase_reference_type_purchase_request = ReferenceTypePurchaseRequestCRUD.delete_reference_type_purchase_request_cruds(db,reference_type_purchase_request_id)
    if not erase_reference_type_purchase_request:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_reference_type_purchase_request)

@router.put("/update-reference-type-purchase-request/{reference_type_purchase_request_id}", status_code=202)
def put_reference_type_purchase_request(payload:ReferenceTypePurchaseRequestSchema.MtrReferenceTypePurchaseRequestGetSchema, reference_type_purchase_request_id,db:Session=Depends(get_db)):
    update_reference_type_purchase_request, update_data_new  = ReferenceTypePurchaseRequestCRUD.put_reference_type_purchase_request_cruds(db,payload, reference_type_purchase_request_id)
    if not update_reference_type_purchase_request:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-reference-type-purchase-request/{reference_type_purchase_request_id}", status_code=202)
def patch_reference_type_purchase_request(reference_type_purchase_request_id,db:Session=Depends(get_db)):
    active_reference_type_purchase_request  = ReferenceTypePurchaseRequestCRUD.patch_reference_type_purchase_request_cruds(db, reference_type_purchase_request_id)
    if not active_reference_type_purchase_request:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_reference_type_purchase_request.is_active = not active_reference_type_purchase_request.is_active
    db.commit()
    db.refresh(active_reference_type_purchase_request)
    return CommonResponse.payload(ResponseException(200), active_reference_type_purchase_request.is_active)
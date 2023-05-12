import json
from fastapi import APIRouter,Depends,HTTPException,status, Request
from payloads import CommonResponse
from exceptions.RequestException import ResponseException 
from cruds import AdjustmentReasonCRUD
from schemas import AdjustmentReasonSchema, LoggingSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from configs.database import get_db
import requests

router = APIRouter(tags=["Adjustment Reason"],prefix="/api/general")
url = "http://127.0.0.1:8000/api/general/create-logging"

@router.get("/get-adjustment-reasons", status_code=200)
def get_adjustment_reasons(db:Session=Depends(get_db)):
    adjustment_reasons = AdjustmentReasonCRUD.get_adjustment_reasons_cruds(db,0,100)
    headers = {"created_by": "50650",
               "hitted_api": "get-adjustment-reasons",
               "http_request": "GET",
               "http_response": "",
               "data_context": str(adjustment_reasons),
               "triggered_menu": "get-adjustment-reasons"}
    if not adjustment_reasons:
        headers["http_response"] = "404"
        requests.post(url, json=headers)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    i = 1
    while i < 100 :
        headers["http_response"] = "200"
        requests.post(url, json=headers)
        i += 1
    return CommonResponse.payloads(ResponseException(200),adjustment_reasons)

@router.get("/get-adjustment-reason/{adjustment_reason_id}", status_code=status.HTTP_200_OK)
def get_adjustment_reason(adjustment_reason_id, db:Session=Depends(get_db)):
    adjustment_reason = AdjustmentReasonCRUD.get_adjustment_reason_cruds(db, adjustment_reason_id)
    headers = {"created_by": "50650",
               "hitted_api": "get-adjustment-reason",
               "http_request": "GET",
               "http_response": "",
               "data_context": str(adjustment_reason),
               "triggered_menu": "get-adjustment-reason"}
    if not adjustment_reason:
        headers["http_response"] = "404"
        requests.post(url, json=headers)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    headers["http_response"] = "200"
    requests.post(url, json=headers)
    return CommonResponse.payload(ResponseException(200), adjustment_reason)

@router.post("/create-adjustment-reason", status_code=201)
def post_adjustment_reason(payload:AdjustmentReasonSchema.MtrAdjustmentReasonGetSchema,db:Session=Depends(get_db)):
    try :
        new_adjustment_reason = AdjustmentReasonCRUD.post_adjustment_reasons_cruds(db, payload)
        db.add(new_adjustment_reason)
        db.commit()
        headers = {"created_by": "50650",
               "hitted_api": "create-adjustment-reason",
               "http_request": "POST",
               "http_response": "",
               "data_context": str(new_adjustment_reason),
               "triggered_menu": "create-adjustment-reason"}
    except IntegrityError: 
        db.rollback()
        headers["http_response"] = "409"
        requests.post(url, json=headers)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    headers["http_response"] = "201"
    requests.post(url, json=headers)
    db.refresh(new_adjustment_reason)
    return CommonResponse.payload(ResponseException(201), new_adjustment_reason)

@router.delete("/delete-adjustment-reason/{adjustment_reason_id}", status_code=202)
def delete_adjustment_reason(adjustment_reason_id, db:Session=Depends(get_db)):
    erase_adjustment_reason = AdjustmentReasonCRUD.delete_adjustment_reason_cruds(db,adjustment_reason_id)
    headers = {"created_by": "50650",
               "hitted_api": "delete-adjustment-reason",
               "http_request": "DELETE",
               "http_response": "",
               "data_context": str(erase_adjustment_reason),
               "triggered_menu": "delete-adjustment-reason"}
    if not erase_adjustment_reason:
        db.rollback()
        headers["http_response"] = "404"
        requests.post(url, json=headers)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    headers["http_response"] = "202"
    requests.post(url, json=headers)
    return CommonResponse.payload(ResponseException(202), erase_adjustment_reason)

@router.put("/update-adjustment-reason/{adjustment_reason_id}", status_code=202)
def put_adjustment_reason(payload:AdjustmentReasonSchema.MtrAdjustmentReasonGetSchema, adjustment_reason_id,db:Session=Depends(get_db)):
    update_adjustment_reason, update_data_new  = AdjustmentReasonCRUD.put_adjustment_reason_cruds(db,payload, adjustment_reason_id)
    headers = {"created_by": "50650",
               "hitted_api": "update-adjustment-reason",
               "http_request": "UPDATE",
               "http_response": "",
               "data_context": str(update_adjustment_reason),
               "triggered_menu": "update-adjustment-reason"}
    if not update_adjustment_reason:
        db.rollback()
        headers["http_response"] = "404"
        requests.post(url, json=headers)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    headers["http_response"] = "200"
    requests.post(url, json=headers)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-adjustment-reason/{adjustment_reason_id}", status_code=202)
def patch_adjustment_reason(adjustment_reason_id,db:Session=Depends(get_db)):
    active_adjustment_reason  = AdjustmentReasonCRUD.patch_adjustment_reason_cruds(db, adjustment_reason_id)
    headers = {"created_by": "50650",
               "hitted_api": "patch-adjustment-reason",
               "http_request": "PATCH",
               "http_response": "",
               "data_context": str(active_adjustment_reason),
               "triggered_menu": "patch-adjustment-reason"}
    if not active_adjustment_reason:
        db.rollback()
        headers["http_response"] = "404"
        requests.post(url, json=headers)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_adjustment_reason.is_active = not active_adjustment_reason.is_active
    db.commit()
    db.refresh(active_adjustment_reason)
    headers["http_response"] = "200"
    requests.post(url, json=headers)
    return CommonResponse.payload(ResponseException(200), active_adjustment_reason.is_active)

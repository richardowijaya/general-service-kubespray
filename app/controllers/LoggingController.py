from datetime import datetime
from fastapi import APIRouter,Depends,HTTPException,status, Request
from cruds import LoggingCRUD
from exceptions.RequestException import ResponseException
from schemas import LoggingSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from configs.database import get_db
from payloads import CommonResponse

router = APIRouter(tags=["Logging"],prefix="/api/general")

@router.get("/get-loggings", status_code=200)
def get_loggings(db:Session=Depends(get_db)):
    loggings = LoggingCRUD.get_loggings_cruds(db,0,100)
    if not loggings:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),loggings)

@router.get("/get-logging/{logging_id}", status_code=200)
def get_logging(logging_id, db:Session=Depends(get_db)):
    logging = LoggingCRUD.get_logging_cruds(db, logging_id)
    if not logging:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),logging)

@router.post("/create-logging", status_code=201)
def post_logging(payload:LoggingSchema.MtrLoggingPostSchema, request:Request, db:Session=Depends(get_db)):
    try:
        new_logging = LoggingCRUD.post_loggings_cruds(payload, request)
        db.add(new_logging)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_logging)
    return CommonResponse.payload(ResponseException(201), new_logging)

@router.delete("/delete-logging/{logging_id}", status_code=202)
def delete_logging(logging_id, db:Session=Depends(get_db)):
    erase_logging = LoggingCRUD.delete_logging_cruds(db,logging_id)
    if not erase_logging:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_logging)

@router.put("/update-logging/{logging_id}", status_code=202)
def put_logging(payload:LoggingSchema.MtrLoggingGetSchema, logging_id,db:Session=Depends(get_db)):
    update_logging, update_data_new  = LoggingCRUD.put_logging_cruds(db,payload, logging_id)
    if not update_logging:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-logging/{logging_id}", status_code=202)
def patch_logging(logging_id,db:Session=Depends(get_db)):
    active_logging  = LoggingCRUD.patch_logging_cruds(db, logging_id)
    if not active_logging:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_logging.is_active = not active_logging.is_active
    db.commit()
    db.refresh(active_logging)
    return CommonResponse.payload(ResponseException(200), active_logging.is_active)

@router.post("/get-ip")
async def log_ip(request: Request):
    client_host = request.client.host
    print(f'ip : {client_host}')

@router.post("/get-time")
async def log_datetime():
    log_time = datetime.now()
    print(f'time : {log_time}')

@router.post("/get-method")
async def log_method(request:Request):
    log_methods = request.method
    print(f'methods : {log_methods}')

@router.post("/get-url")
async def log_path(request:Request):
    log_paths = request.url.path
    print(f'methods : {log_paths}')

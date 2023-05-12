from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import Request
from models import LoggingModel

def get_loggings_cruds(db:Session,offset:int=0, limit:int=100):
    return db.query(LoggingModel.MtrLogging).order_by(LoggingModel.MtrLogging.logging_id).offset(offset).limit(limit).all()


def get_logging_cruds(db:Session,get_id:int):
    return  db.query(LoggingModel.MtrLogging).filter(LoggingModel.MtrLogging.logging_id==get_id).first()
    
def post_loggings_cruds(payload:LoggingModel.MtrLogging, request:Request):
    
    _logging =  LoggingModel.MtrLogging()
    _logging.created_at = datetime.now()
    _logging.created_by = payload.created_by
    _logging.hitted_api = payload.hitted_api
    _logging.http_request = payload.http_request
    _logging.http_response = payload.http_response
    _logging.data_context = payload.data_context
    _logging.triggered_menu = payload.triggered_menu
    _logging.ip_address = request.client.host
    print(_logging)
    return _logging

def delete_logging_cruds(db:Session,get_id:int):
    return db.query(LoggingModel.MtrLogging).filter(LoggingModel.MtrLogging.logging_id==get_id).delete(synchronize_session=False)
    
def put_logging_cruds(db:Session,payload:LoggingModel.MtrLogging, get_id:int):
    edit_logging = db.query(LoggingModel.MtrLogging).filter(LoggingModel.MtrLogging.logging_id==get_id)
    edit_logging.update(payload.dict())
    message_logging = edit_logging.first()
    return edit_logging, message_logging

def patch_logging_cruds(db:Session, get_id:int):
    return db.query(LoggingModel.MtrLogging).filter(LoggingModel.MtrLogging.logging_id==get_id).first()

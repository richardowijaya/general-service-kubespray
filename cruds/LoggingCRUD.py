from sqlalchemy.orm import Session
from models import LoggingModel

def get_loggings_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(LoggingModel.MtrLogging).order_by(LoggingModel.MtrLogging.logging_id).offset(offset).limit(limit).all()


def get_logging_cruds(db:Session,get_id:int):
    return  db.query(LoggingModel.MtrLogging).filter(LoggingModel.MtrLogging.logging_id==get_id).first()
    

def post_logging_cruds(db:Session, payload:LoggingModel.MtrLogging):
    return LoggingModel.MtrLogging(**payload.dict())

def delete_logging_cruds(db:Session,get_id:int):
    return db.query(LoggingModel.MtrLogging).filter(LoggingModel.MtrLogging.logging_id==get_id).delete(synchronize_session=False)
    
def put_logging_cruds(db:Session,payload:LoggingModel.MtrLogging, get_id:int):
    edit_logging = db.query(LoggingModel.MtrLogging).filter(LoggingModel.MtrLogging.logging_id==get_id)
    edit_logging.update(payload.dict())
    messages_logging = edit_logging.first()
    return edit_logging, messages_logging

def patch_logging_cruds(db:Session, get_id:int):
    return db.query(LoggingModel.MtrLogging).filter(LoggingModel.MtrLogging.logging_id==get_id).first()

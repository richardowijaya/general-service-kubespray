from sqlalchemy.orm import Session
from models import JobPositionModel

def get_job_positions_cruds(db:Session,offset:int=0, limit:int=100):
    return db.query(JobPositionModel.MtrJobPosition).order_by(JobPositionModel.MtrJobPosition.job_position_id).offset(offset).limit(limit).all()


def get_job_position_cruds(db:Session,get_id:int):
    return  db.query(JobPositionModel.MtrJobPosition).filter(JobPositionModel.MtrJobPosition.job_position_id==get_id).first()
    

def post_job_position_cruds(db:Session, payload:JobPositionModel.MtrJobPosition):
    return JobPositionModel.MtrJobPosition(**payload.dict())

def delete_job_position_cruds(db:Session,get_id:int):
    return db.query(JobPositionModel.MtrJobPosition).filter(JobPositionModel.MtrJobPosition.job_position_id==get_id).delete(synchronize_session=False)
    
def put_job_position_cruds(db:Session,payload:JobPositionModel.MtrJobPosition, get_id:int):
    edit_job_position = db.query(JobPositionModel.MtrJobPosition).filter(JobPositionModel.MtrJobPosition.job_position_id==get_id)
    edit_job_position.update(payload.dict())
    message_job_position = edit_job_position.first()
    return edit_job_position, message_job_position

def patch_job_position_cruds(db:Session, get_id:int):
    return db.query(JobPositionModel.MtrJobPosition).filter(JobPositionModel.MtrJobPosition.job_position_id==get_id).first()

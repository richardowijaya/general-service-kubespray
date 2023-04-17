from sqlalchemy.orm import Session
from models import JobTitleModel

def get_job_titles_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(JobTitleModel.MtrJobTitle).order_by(JobTitleModel.MtrJobTitle.job_title_id).offset(offset).limit(limit).all()


def get_job_title_cruds(db:Session,get_id:int):
    return  db.query(JobTitleModel.MtrJobTitle).filter(JobTitleModel.MtrJobTitle.job_title_id==get_id).first()
    

def post_job_title_cruds(db:Session, payload:JobTitleModel.MtrJobTitle):
    return JobTitleModel.MtrJobTitle(**payload.dict())

def delete_job_title_cruds(db:Session,get_id:int):
    return db.query(JobTitleModel.MtrJobTitle).filter(JobTitleModel.MtrJobTitle.job_title_id==get_id).delete(synchronize_session=False)
    
def put_job_title_cruds(db:Session,payload:JobTitleModel.MtrJobTitle, get_id:int):
    edit_job_title = db.query(JobTitleModel.MtrJobTitle).filter(JobTitleModel.MtrJobTitle.job_title_id==get_id)
    edit_job_title.update(payload.dict())
    messages_job_title = edit_job_title.first()
    return edit_job_title, messages_job_title

def patch_job_title_cruds(db:Session, get_id:int):
    return db.query(JobTitleModel.MtrJobTitle).filter(JobTitleModel.MtrJobTitle.job_title_id==get_id).first()

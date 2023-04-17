from sqlalchemy.orm import Session
from models import IncentiveLevelModel

def get_incentive_levels_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(IncentiveLevelModel.MtrIncentiveLevel).order_by(IncentiveLevelModel.MtrIncentiveLevel.incentive_level_id).offset(offset).limit(limit).all()


def get_incentive_level_cruds(db:Session,get_id:int):
    return  db.query(IncentiveLevelModel.MtrIncentiveLevel).filter(IncentiveLevelModel.MtrIncentiveLevel.incentive_level_id==get_id).first()
    

def post_incentive_level_cruds(db:Session, payload:IncentiveLevelModel.MtrIncentiveLevel):
    return IncentiveLevelModel.MtrIncentiveLevel(**payload.dict())

def delete_incentive_level_cruds(db:Session,get_id:int):
    return db.query(IncentiveLevelModel.MtrIncentiveLevel).filter(IncentiveLevelModel.MtrIncentiveLevel.incentive_level_id==get_id).delete(synchronize_session=False)
    
def put_incentive_level_cruds(db:Session,payload:IncentiveLevelModel.MtrIncentiveLevel, get_id:int):
    edit_incentive_level = db.query(IncentiveLevelModel.MtrIncentiveLevel).filter(IncentiveLevelModel.MtrIncentiveLevel.incentive_level_id==get_id)
    edit_incentive_level.update(payload.dict())
    messages_incentive_level = edit_incentive_level.first()
    return edit_incentive_level, messages_incentive_level

def patch_incentive_level_cruds(db:Session, get_id:int):
    return db.query(IncentiveLevelModel.MtrIncentiveLevel).filter(IncentiveLevelModel.MtrIncentiveLevel.incentive_level_id==get_id).first()

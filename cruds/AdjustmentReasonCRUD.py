from sqlalchemy.orm import Session
from models import AdjustmentReasonModel

<<<<<<< HEAD
def get_adjustment_reasons_cruds(db:Session, offset:int=0, limit:int=100):
=======
def get_adjustment_reasons_cruds(db:Session,offset:int=0, limit:int=100):
>>>>>>> 6c332901c44706e2cd630677bcf753c81a5cd6b3
    return db.query(AdjustmentReasonModel.MtrAdjustmentReason).order_by(AdjustmentReasonModel.MtrAdjustmentReason.adjustment_reason_id).offset(offset).limit(limit).all()


def get_adjustment_reason_cruds(db:Session,get_id:int):
    return  db.query(AdjustmentReasonModel.MtrAdjustmentReason).filter(AdjustmentReasonModel.MtrAdjustmentReason.adjustment_reason_id==get_id).first()
    

def post_adjustment_reasons_cruds(db:Session, payload:AdjustmentReasonModel.MtrAdjustmentReason):
    return AdjustmentReasonModel.MtrAdjustmentReason(**payload.dict())

def delete_adjustment_reason_cruds(db:Session,get_id:int):
    return db.query(AdjustmentReasonModel.MtrAdjustmentReason).filter(AdjustmentReasonModel.MtrAdjustmentReason.adjustment_reason_id==get_id).delete(synchronize_session=False)
    
def put_adjustment_reason_cruds(db:Session,payload:AdjustmentReasonModel.MtrAdjustmentReason, get_id:int):
    edit_adjustment_reason = db.query(AdjustmentReasonModel.MtrAdjustmentReason).filter(AdjustmentReasonModel.MtrAdjustmentReason.adjustment_reason_id==get_id)
    edit_adjustment_reason.update(payload.dict())
    message_adjustment_reason = edit_adjustment_reason.first()
    return edit_adjustment_reason, message_adjustment_reason

def patch_adjustment_reason_cruds(db:Session, get_id:int):
    return db.query(AdjustmentReasonModel.MtrAdjustmentReason).filter(AdjustmentReasonModel.MtrAdjustmentReason.adjustment_reason_id==get_id).first()

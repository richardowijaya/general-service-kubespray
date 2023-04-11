from sqlalchemy.orm import Session
from models import AdjustmentReasonModel

def get_adjustment_reasons_cruds(db:Session):
    adjustment_reasons = db.query(AdjustmentReasonModel.MtrAdjustmentReason).all()
    return adjustment_reasons

def get_adjustment_reason_cruds(db:Session,get_id:int):
    adjustment_reason = db.query(AdjustmentReasonModel.MtrAdjustmentReason).filter(AdjustmentReasonModel.MtrAdjustmentReason.adjustment_reason_id==get_id).first()
    return adjustment_reason

def post_adjustment_reasons_cruds(db:Session, payload:AdjustmentReasonModel.MtrAdjustmentReason):
    new_adjustment_reason = AdjustmentReasonModel.MtrAdjustmentReason(**payload.dict())
    return new_adjustment_reason

def delete_adjustment_reason_cruds(db:Session,get_id:int):
    erase_adjustment_reason = db.query(AdjustmentReasonModel.MtrAdjustmentReason).filter(AdjustmentReasonModel.MtrAdjustmentReason.adjustment_reason_id==get_id).delete(synchronize_session=False)
    return erase_adjustment_reason

def put_adjustment_reason_cruds(db:Session,payload:AdjustmentReasonModel.MtrAdjustmentReason, get_id:int):
    edit_adjustment_reason = db.query(AdjustmentReasonModel.MtrAdjustmentReason).filter(AdjustmentReasonModel.MtrAdjustmentReason.adjustment_reason_id==get_id)
    edit_adjustment_reason.update(payload.dict())
    message_edit_adjustment_reason= edit_adjustment_reason.first()
    return edit_adjustment_reason, message_edit_adjustment_reason

def patch_adjustment_reason_cruds(db:Session, get_id:int):
    active_adjustment_reason = db.query(AdjustmentReasonModel.MtrAdjustmentReason).filter(AdjustmentReasonModel.MtrAdjustmentReason.adjustment_reason_id==get_id).first()
    active_adjustment_reason.is_active = not active_adjustment_reason.is_active
    return active_adjustment_reason
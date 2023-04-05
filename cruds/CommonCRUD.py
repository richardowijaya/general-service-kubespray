from sqlalchemy.orm import Session
from models import CommonModel

def get_adjustment_reasons_cruds(db:Session):
    adjustment_reasons = db.query(CommonModel.MtrAdjustmentReason).all()
    return adjustment_reasons

def post_adjustment_reasons_cruds(payload:CommonModel.MtrAdjustmentReason,db:Session):
    new_adjsument_reason = CommonModel.MtrAdjustmentReason(**payload.dict())
    if new_adjsument_reason.is_active==True:
        new_adjsument_reason.is_active = 1
    else:
        new_adjsument_reason.is_active = 0
    return new_adjsument_reason

def get_adjustment_reasons_by_id_cruds(db:Session,get_id:int):
    adjustment_reasons = db.query(CommonModel.MtrAdjustmentReason).filter(CommonModel.MtrAdjustmentReason.adjustment_reason_id==get_id)
    return adjustment_reasons

def update_adjustment_reasons_cruds(payload:CommonModel.MtrAdjustmentReason,db:Session):
    update_adjustment_reasons = CommonModel.MtrAdjustmentReason(**payload.dict())    

def get_aftersales_area_cruds(db:Session):
    aftersales_areas = db.query(CommonModel.MtrAftersalesArea).all()
    return aftersales_areas

def post_aftersales_area_cruds(payload:CommonModel.MtrAftersalesArea,db:Session):
    new_aftersales_area = CommonModel.MtrAftersalesArea(**payload.dict())
    if new_aftersales_area.is_active==True:
        new_aftersales_area.is_active = 1
    else:
        new_aftersales_area.is_active = 0
    return new_aftersales_area

def get_new_aftersales_area_by_id_cruds(db:Session,get_id:int):
    aftersales_area = db.query(CommonModel.MtrAftersalesArea).filter(CommonModel.MtrAftersalesArea.aftersales_area_id==get_id)
    return aftersales_area

def update_aftersales_area_cruds(payload:CommonModel.MtrAftersalesArea,db:Session):
    update_aftersales_area = CommonModel.MtrAftersalesArea(**payload.dict())    
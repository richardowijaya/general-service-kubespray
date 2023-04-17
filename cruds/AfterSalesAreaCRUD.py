from sqlalchemy.orm import Session
from models import AfterSalesAreaModel

def get_aftersales_area_cruds(db:Session):
    aftersales_areas = db.query(AfterSalesAreaModel.MtrAftersalesArea).all()
    return aftersales_areas

def post_aftersales_area_cruds(payload:AfterSalesAreaModel.MtrAftersalesArea,db:Session):
    new_aftersales_area = AfterSalesAreaModel.MtrAftersalesArea(**payload.dict())
    if new_aftersales_area.is_active==True:
        new_aftersales_area.is_active = 1
    else:
        new_aftersales_area.is_active = 0
    return new_aftersales_area

def get_new_aftersales_area_by_id_cruds(db:Session,get_id:int):
    aftersales_area = db.query(AfterSalesAreaModel.MtrAftersalesArea).filter(AfterSalesAreaModel.MtrAftersalesArea.aftersales_area_id==get_id)
    return aftersales_area

def update_aftersales_area_cruds(payload:AfterSalesAreaModel.MtrAftersalesArea,db:Session):
    update_aftersales_area = AfterSalesAreaModel.MtrAftersalesArea(**payload.dict())    
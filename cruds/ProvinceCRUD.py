from sqlalchemy.orm import Session
from models import ProvinceModel

def get_provinces_cruds(db:Session):
    provinces = db.query(ProvinceModel.MtrProvince).all()
    return provinces

def get_province_id(db:Session,get_id:int):
    province = db.query(ProvinceModel.MtrProvince).filter(ProvinceModel.MtrProvince.province_id==get_id)
    return province

def post_provinces_cruds(payload:ProvinceModel.MtrProvince):
    new_data = ProvinceModel.MtrProvince(**payload.dict())
    if new_data.is_active == True:
        new_data.is_active = 1
    else:
        new_data.is_active = 0
    return new_data

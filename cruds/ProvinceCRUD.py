from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from models import ProvinceModel

def get_provinces_cruds(db:Session):
    provinces = db.query(ProvinceModel.MtrProvince).all()
    return provinces

def get_province_id(db:Session,get_id:int):
    province = db.query(ProvinceModel.MtrProvince).filter(ProvinceModel.MtrProvince.province_id==get_id)
    return province

def post_provinces_cruds(payload:ProvinceModel.MtrProvince):
    new_data = payload(**payload.dict())
    if new_data.is_active == True:
        new_data.is_active = 1
    else:
        new_data.is_active = 0
    return new_data

def delete_province_crud(del_id:int,db:Session):
    check_id = db.query(ProvinceModel.MtrProvince).filter(ProvinceModel.MtrProvince.province_id==del_id).first()
    return check_id

def update_province_cruds(payload:ProvinceModel.MtrProvince,edit_id:int,db:Session):
    check_id = db.query(payload).filter(payload.province_id==edit_id)
    return check_id

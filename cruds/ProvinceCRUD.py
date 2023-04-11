from sqlalchemy.orm import Session
from models import ProvinceModel
from schemas import ProvinceSchema

#get all data
def get_province_all(db:Session,skip:int=0,limit:int=100):
    return db.query(ProvinceModel.MtrProvince).offset(skip).limit(limit).all()

#get data by filtering the primary_key(ID)
def get_province_by_id(db:Session,get_id:int):
    return db.query(ProvinceModel.MtrProvince).filter(ProvinceModel.MtrProvince.province_id==get_id).first()

#post / create new data
def post_new_province(db:Session,province:ProvinceSchema.MtrProvinceSchema):
    _province = ProvinceModel.MtrProvince()
    _province.province_code = province.province_code
    _province.province_name = province.province_name
    _province.country_id = province.country_id
    db.add(_province)
    db.commit()
    db.refresh(_province)
    print(_province)
    return _province

#delete data by primary_key(ID)
def del_province(db:Session,del_id:int):
    _province = get_province_by_id(db=db,get_id=del_id)
    db.delete(_province)
    db.commit()
    return {
        "status_code":200,
        "msg_status":"deleted"
    }

#update data by primary_key(ID)
def update_province(db:Session,update_id:int,province:ProvinceSchema.MtrProvinceSchema):
    _province = get_province_by_id(db,update_id)
    _province.province_code = province.province_code
    _province.province_name = province.province_name
    _province.country_id = province.country_id
    db.commit()
    db.refresh(_province)
    return _province
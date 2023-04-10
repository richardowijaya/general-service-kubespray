from sqlalchemy.orm import Session
from models import CountryModel

def get_countries_cruds(db:Session):
    countries = db.query(CountryModel.MtrCountry).all()
    return countries

def get_country_id(db:Session,get_id:int):
    province = db.query(CountryModel.MtrCountry).filter(CountryModel.MtrCountry.country_id==get_id).first()
    return province

def post_country_cruds(payload:CountryModel.MtrCountry):
    new_data = CountryModel.MtrCountry(**payload.dict())
    if new_data.is_active == True:
        new_data.is_active = 1
    else:
        new_data.is_active = 0
    return new_data

def delete_country_crud(del_id:int,db:Session):
    check_id = db.query(CountryModel.MtrCountry).filter(CountryModel.MtrCountry.country_id==del_id).first()
    return check_id

def update_country_cruds(edit_id:int,db:Session):
    check_id = db.query(CountryModel).filter(CountryModel.MtrCountry.province_id==edit_id)
    return check_id
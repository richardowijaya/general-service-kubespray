from sqlalchemy.orm import Session
from models import CountryModel

def get_countries_cruds(db:Session):
    countries = db.query(CountryModel.MtrCountry).all()
    return countries

def post_new_country_cruds(payload:CountryModel.MtrCountry,db:Session):
    new_country = CountryModel.MtrCountry(**payload.dict())
    if new_country.is_active==True:
        new_country.is_active = 1
    else:
        new_country.is_active = 0
    return new_country

def get_country_cruds(db:Session,get_id:int):
    country = db.query(CountryModel.MtrCountry).filter(CountryModel.MtrCountry.country_id==get_id)
    return country

def update_new_country_cruds(payload:CountryModel.MtrCountry,db:Session):
    update_country = CountryModel.MtrCountry(**payload.dict())    
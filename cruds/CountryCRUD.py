from sqlalchemy.orm import Session
from models import CountryModel 
from schemas import CountrySchema

#get all data
def get_country_all(db:Session,skip:int=0,limit:int=100):
    return db.query(CountryModel.MtrCountry).order_by(CountryModel.MtrCountry.country_id).offset(skip).limit(limit).all()

#get data by filtering the primary_key(ID)
def get_country_by_id(db:Session,get_id:int):
    return db.query(CountryModel.MtrCountry).filter(CountryModel.MtrCountry.country_id==get_id).first()

#post / create new data
def post_new_country(db:Session,country:CountrySchema.MtrCountrySchema):
    _country = CountryModel.MtrCountry()
    _country.country_code = country.country_code
    _country.country_name = country.country_name
    _country.country_language = country.country_language
    _country.country_phone = country.country_phone
    _country.currency_id = country.currency_id
    db.add(_country)
    db.commit()
    db.refresh(_country)
    #print(_country)
    return _country

#delete data by primary_key(ID)
def del_country(db:Session,del_id:int):
    _country = get_country_by_id(db=db,get_id=del_id)
    db.delete(_country)
    db.commit()
    return {
        "status_code":200,
        "msg_status":"deleted"
    }

#update data by primary_key(ID)
def update_country(db:Session,update_id:int,country:CountrySchema.MtrCountrySchema):
    _country = get_country_by_id(db,update_id)
    _country.country_code = country.country_code
    _country.country_name = country.country_name
    _country.country_language = country.country_language
    _country.country_phone = country.country_phone
    _country.currency_id = country.currency_id
    db.commit()
    db.refresh(_country)
    return _country
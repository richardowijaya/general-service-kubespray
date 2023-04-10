from sqlalchemy.orm import Session
from models import RegionModel 
from schemas import RegionSchema

#get all data
def get_region_all(db:Session,skip:int=0,limit:int=100):
    return db.query(RegionModel.MtrRegion).offset(skip).limit(limit).all()

#get data by filtering the primary_key(ID)
def get_region_by_id(db:Session,get_id:int):
    return db.query(RegionModel.MtrRegion).filter(RegionModel.MtrRegion.regional_id==get_id).first()

#post / create new data
def post_new_region(db:Session,region:RegionSchema.MtrRegionSchema):
    _region = RegionModel.MtrRegion()
    _region.regional_code = region.regional_code
    _region.regional_name = region.regional_name
    _region.user_id = region.user_id
    db.add(_region)
    db.commit()
    db.refresh(_region)
    print(_region)
    return _region

#delete data by primary_key(ID)
def del_region(db:Session,del_id:int):
    _region = get_region_by_id(db=db,get_id=del_id)
    db.delete(_region)
    db.commit()
    return {
        "status_code":200,
        "msg_status":"deleted"
    }

#update data by primary_key(ID)
def update_region(db:Session,update_id:int,region:RegionSchema.MtrRegionSchema):
    _region = get_region_by_id(db,update_id)
    _region.regional_code = region.regional_code
    _region.regional_name = region.regional_name
    _region.user_id = region.user_id
    db.commit()
    db.refresh(_region)
    return _region
from sqlalchemy.orm import Session
from models import AreaModel
from schemas import AreaSchema

#get all data
def get_area_all(db:Session,skip:int=0,limit:int=100):
<<<<<<< HEAD
    return db.query(AreaModel.MtrArea).order_by(AreaModel.MtrArea.area_id).offset(skip).limit(limit).all()
=======
    return db.query(AreaModel.MtrArea).offset(skip).limit(limit).all()
>>>>>>> 6c332901c44706e2cd630677bcf753c81a5cd6b3

#get data by filtering the primary_key(ID)
def get_area_by_id(db:Session,get_id:int):
    return db.query(AreaModel.MtrArea).filter(AreaModel.MtrArea.area_id==get_id).first()

#post / create new data
def post_new_area(db:Session,area:AreaSchema.MtrAreaSchema):
    _area = AreaModel.MtrArea()
    _area.area_code = area.area_code
    _area.description = area.description
<<<<<<< HEAD
    _area.region_id = area.region_id
=======
    _area.regional_id = area.regional_id
>>>>>>> 6c332901c44706e2cd630677bcf753c81a5cd6b3
    db.add(_area)
    db.commit()
    db.refresh(_area)
    print(_area)
    return _area

#delete data by primary_key(ID)
def del_area(db:Session,del_id:int):
    _area = get_area_by_id(db=db,get_id=del_id)
    db.delete(_area)
    db.commit()
    return {
        "status_code":200,
        "msg_status":"deleted"
    }

#update data by primary_key(ID)
def update_area(db:Session,update_id:int,area:AreaSchema.MtrAreaSchema):
    _area = get_area_by_id(db,update_id)
    _area.area_code = area.area_code
    _area.description = area.description
<<<<<<< HEAD
    _area.region_id = area.region_id
=======
    _area.regional_id = area.regional_id
>>>>>>> 6c332901c44706e2cd630677bcf753c81a5cd6b3
    db.commit()
    db.refresh(_area)
    return _area
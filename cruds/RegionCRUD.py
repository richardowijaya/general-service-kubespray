from sqlalchemy.orm import Session
from models import RegionModel

def get_regioncruds(db:Session):
    results = db.query(RegionModel.MtrRegion).all()
    return results

def post_regioncruds(payload:RegionModel.MtrRegion,db:Session):
    new_region = RegionModel.MtrRegion(**payload.dict())
    if new_region.is_active == True:
        new_region.is_active = 1
    else:
        new_region.is_active = 0
    return new_region
from sqlalchemy.orm import Session
from sqlalchemy import select, column
from models import RegionModel 
from schemas import RegionSchema

#get all data
def get_region_all(db:Session,skip:int,limit:int,query:list[str]):
    query_data = db.query(RegionModel.MtrRegion).all()
    
    if skip == None:
        page = 1
        page_limit = 5
    else:
        page = skip
        page_limit = limit 
    total_rows = len(query_data)
    total_pages = int(total_rows/page_limit)

    results = db.query(RegionModel.MtrRegion).order_by(RegionModel.MtrRegion.region_id).offset(skip).limit(limit).all()

    query_check = select(RegionModel.MtrRegion).order_by(RegionModel.MtrRegion.region_id)

    hasil = db.execute(str(query_check)).all()
    print(str(hasil))

    '''
    from sqlmodel import Session, column, select
    from models.RegionModel import Region


    def get_all_users(session: Session, skip: int = 0, limit: int = 100, filter: list[str] = [], filterParam: list[str] = []):
        print(filterParam)
        print(filter)
        region = select(Region).order_by(Region.region_id).offset(skip).limit(limit)

        if (len(filter) > 0):
            for idx, x in enumerate(filter):

                if (filterParam[idx] == "is_active"):
                    region = region.where(column(filterParam[idx]) == bool(filter[idx]))
                    continue

                region = region.where(column(filterParam[idx]).contains(filter[idx]))

        return session.exec(region).all()
    '''


    #checking any filter that send to back-end
    query_results = db.query(RegionModel.MtrRegion).filter(RegionModel.MtrRegion.region_code.like("%"+query[0]+"%"),
                                                           RegionModel.MtrRegion.region_name.like("%"+query[1]+"%")).order_by(RegionModel.MtrRegion.region_id).offset(skip).limit(limit).all()

    return page,page_limit,total_rows,total_pages,hasil

#get data by filtering the primary_key(ID)
def get_region_by_id(db:Session,get_id:int):
    return db.query(RegionModel.MtrRegion).filter(RegionModel.MtrRegion.region_id==get_id).first()

#get data by filtering the param(s)
def get_region_by_params(db:Session,code):
    return db.query(RegionModel.MtrRegion).filter(RegionModel.MtrRegion.region_code==code).all()


#post / create new data
def post_new_region(db:Session,region:RegionSchema.MtrRegionSchema):
    _region = RegionModel.MtrRegion()
    _region.region_code = region.region_code
    _region.region_name = region.region_name
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
    _region.region_code = region.region_code
    _region.region_name = region.region_name
    _region.user_id = region.user_id
    db.commit()
    db.refresh(_region)
    return _region
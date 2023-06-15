from sqlalchemy.orm import Session
from models import BrandTypeModel

def get_brand_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(BrandTypeModel.MtrBrandType).order_by(BrandTypeModel.MtrBrandType.brand_type_id).offset(offset).limit(limit).all()


def get_brand_type_cruds(db:Session,get_id:int):
    return  db.query(BrandTypeModel.MtrBrandType).filter(BrandTypeModel.MtrBrandType.brand_type_id==get_id).first()
    

def post_brand_type_cruds(db:Session, payload:BrandTypeModel.MtrBrandType):
    return BrandTypeModel.MtrBrandType(**payload.dict())

def delete_brand_type_cruds(db:Session,get_id:int):
    return db.query(BrandTypeModel.MtrBrandType).filter(BrandTypeModel.MtrBrandType.brand_type_id==get_id).delete(synchronize_session=False)
    
def put_brand_type_cruds(db:Session,payload:BrandTypeModel.MtrBrandType, get_id:int):
    edit_brand_type = db.query(BrandTypeModel.MtrBrandType).filter(BrandTypeModel.MtrBrandType.brand_type_id==get_id)
    edit_brand_type.update(payload.dict())
    messages_brand_type = edit_brand_type.first()
    return edit_brand_type, messages_brand_type

def patch_brand_type_cruds(db:Session, get_id:int):
    return db.query(BrandTypeModel.MtrBrandType).filter(BrandTypeModel.MtrBrandType.brand_type_id==get_id).first()

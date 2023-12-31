from sqlalchemy.orm import Session
from models import BusinessTypeModel

def get_business_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(BusinessTypeModel.MtrBusinessType).order_by(BusinessTypeModel.MtrBusinessType.business_type_id).offset(offset).limit(limit).all()


def get_business_type_cruds(db:Session,get_id:int):
    return  db.query(BusinessTypeModel.MtrBusinessType).filter(BusinessTypeModel.MtrBusinessType.business_type_id==get_id).first()
    

def post_business_type_cruds(db:Session, payload:BusinessTypeModel.MtrBusinessType):
    return BusinessTypeModel.MtrBusinessType(**payload.dict())

def delete_business_type_cruds(db:Session,get_id:int):
    return db.query(BusinessTypeModel.MtrBusinessType).filter(BusinessTypeModel.MtrBusinessType.business_type_id==get_id).delete(synchronize_session=False)
    
def put_business_type_cruds(db:Session,payload:BusinessTypeModel.MtrBusinessType, get_id:int):
    edit_business_type = db.query(BusinessTypeModel.MtrBusinessType).filter(BusinessTypeModel.MtrBusinessType.business_type_id==get_id)
    edit_business_type.update(payload.dict())
    messages_business_type = edit_business_type.first()
    return edit_business_type, messages_business_type

def patch_business_type_cruds(db:Session, get_id:int):
    return db.query(BusinessTypeModel.MtrBusinessType).filter(BusinessTypeModel.MtrBusinessType.business_type_id==get_id).first()

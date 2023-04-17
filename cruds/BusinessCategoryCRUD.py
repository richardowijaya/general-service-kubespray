from sqlalchemy.orm import Session
from models import BusinessCategoryModel

def get_business_categories_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(BusinessCategoryModel.MtrBusinessCategory).order_by(BusinessCategoryModel.MtrBusinessCategory.business_category_id).offset(offset).limit(limit).all()


def get_business_category_cruds(db:Session,get_id:int):
    return  db.query(BusinessCategoryModel.MtrBusinessCategory).filter(BusinessCategoryModel.MtrBusinessCategory.business_category_id==get_id).first()
    

def post_business_category_cruds(db:Session, payload:BusinessCategoryModel.MtrBusinessCategory):
    return BusinessCategoryModel.MtrBusinessCategory(**payload.dict())

def delete_business_category_cruds(db:Session,get_id:int):
    return db.query(BusinessCategoryModel.MtrBusinessCategory).filter(BusinessCategoryModel.MtrBusinessCategory.business_category_id==get_id).delete(synchronize_session=False)
    
def put_business_category_cruds(db:Session,payload:BusinessCategoryModel.MtrBusinessCategory, get_id:int):
    edit_business_category = db.query(BusinessCategoryModel.MtrBusinessCategory).filter(BusinessCategoryModel.MtrBusinessCategory.business_category_id==get_id)
    edit_business_category.update(payload.dict())
    messages_business_category = edit_business_category.first()
    return edit_business_category, messages_business_category

def patch_business_category_cruds(db:Session, get_id:int):
    return db.query(BusinessCategoryModel.MtrBusinessCategory).filter(BusinessCategoryModel.MtrBusinessCategory.business_category_id==get_id).first()

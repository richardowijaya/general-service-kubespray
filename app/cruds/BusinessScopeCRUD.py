from sqlalchemy.orm import Session
from models import BusinessScopeModel

def get_business_scopes_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(BusinessScopeModel.MtrBusinessScope).order_by(BusinessScopeModel.MtrBusinessScope.business_scope_id).offset(offset).limit(limit).all()


def get_business_scope_cruds(db:Session,get_id:int):
    return  db.query(BusinessScopeModel.MtrBusinessScope).filter(BusinessScopeModel.MtrBusinessScope.business_scope_id==get_id).first()
    

def post_business_scope_cruds(db:Session, payload:BusinessScopeModel.MtrBusinessScope):
    return BusinessScopeModel.MtrBusinessScope(**payload.dict())

def delete_business_scope_cruds(db:Session,get_id:int):
    return db.query(BusinessScopeModel.MtrBusinessScope).filter(BusinessScopeModel.MtrBusinessScope.business_scope_id==get_id).delete(synchronize_session=False)
    
def put_business_scope_cruds(db:Session,payload:BusinessScopeModel.MtrBusinessScope, get_id:int):
    edit_business_scope = db.query(BusinessScopeModel.MtrBusinessScope).filter(BusinessScopeModel.MtrBusinessScope.business_scope_id==get_id)
    edit_business_scope.update(payload.dict())
    messages_business_scope = edit_business_scope.first()
    return edit_business_scope, messages_business_scope

def patch_business_scope_cruds(db:Session, get_id:int):
    return db.query(BusinessScopeModel.MtrBusinessScope).filter(BusinessScopeModel.MtrBusinessScope.business_scope_id==get_id).first()

from sqlalchemy.orm import Session
from models import SubstituteTypeModel

def get_substitute_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(SubstituteTypeModel.MtrSubstituteType).order_by(SubstituteTypeModel.MtrSubstituteType.substitute_type_id).offset(offset).limit(limit).all()


def get_substitute_type_cruds(db:Session,get_id:int):
    return  db.query(SubstituteTypeModel.MtrSubstituteType).filter(SubstituteTypeModel.MtrSubstituteType.substitute_type_id==get_id).first()
    

def post_substitute_type_cruds(db:Session, payload:SubstituteTypeModel.MtrSubstituteType):
    return SubstituteTypeModel.MtrSubstituteType(**payload.dict())

def delete_substitute_type_cruds(db:Session,get_id:int):
    return db.query(SubstituteTypeModel.MtrSubstituteType).filter(SubstituteTypeModel.MtrSubstituteType.substitute_type_id==get_id).delete(synchronize_session=False)
    
def put_substitute_type_cruds(db:Session,payload:SubstituteTypeModel.MtrSubstituteType, get_id:int):
    edit_substitute_type = db.query(SubstituteTypeModel.MtrSubstituteType).filter(SubstituteTypeModel.MtrSubstituteType.substitute_type_id==get_id)
    edit_substitute_type.update(payload.dict())
    messages_substitute_type = edit_substitute_type.first()
    return edit_substitute_type, messages_substitute_type

def patch_substitute_type_cruds(db:Session, get_id:int):
    return db.query(SubstituteTypeModel.MtrSubstituteType).filter(SubstituteTypeModel.MtrSubstituteType.substitute_type_id==get_id).first()

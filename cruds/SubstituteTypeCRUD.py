from sqlalchemy.orm import Session
from models import SubstituteTypeModel

def get_substitue_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(SubstituteTypeModel.MtrSubstituteType).order_by(SubstituteTypeModel.MtrSubstituteType.substitute_type_id).offset(offset).limit(limit).all()


def get_substitue_type_cruds(db:Session,get_id:int):
    return  db.query(SubstituteTypeModel.MtrSubstituteType).filter(SubstituteTypeModel.MtrSubstituteType.substitute_type_id==get_id).first()
    

def post_substitue_type_cruds(db:Session, payload:SubstituteTypeModel.MtrSubstituteType):
    return SubstituteTypeModel.MtrSubstituteType(**payload.dict())

def delete_substitue_type_cruds(db:Session,get_id:int):
    return db.query(SubstituteTypeModel.MtrSubstituteType).filter(SubstituteTypeModel.MtrSubstituteType.substitute_type_id==get_id).delete(synchronize_session=False)
    
def put_substitue_type_cruds(db:Session,payload:SubstituteTypeModel.MtrSubstituteType, get_id:int):
    edit_substitue_type = db.query(SubstituteTypeModel.MtrSubstituteType).filter(SubstituteTypeModel.MtrSubstituteType.substitute_type_id==get_id)
    edit_substitue_type.update(payload.dict())
    messages_substitue_type = edit_substitue_type.first()
    return edit_substitue_type, messages_substitue_type

def patch_substitue_type_cruds(db:Session, get_id:int):
    return db.query(SubstituteTypeModel.MtrSubstituteType).filter(SubstituteTypeModel.MtrSubstituteType.substitute_type_id==get_id).first()

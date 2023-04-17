from sqlalchemy.orm import Session
from models import SkillLevelCodeModel

def get_skill_level_codes_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(SkillLevelCodeModel.MtrSkillLevelCode).order_by(SkillLevelCodeModel.MtrSkillLevelCode.skill_level_code_id).offset(offset).limit(limit).all()


def get_skill_level_code_cruds(db:Session,get_id:int):
    return  db.query(SkillLevelCodeModel.MtrSkillLevelCode).filter(SkillLevelCodeModel.MtrSkillLevelCode.skill_level_code_id==get_id).first()
    

def post_skill_level_code_cruds(db:Session, payload:SkillLevelCodeModel.MtrSkillLevelCode):
    return SkillLevelCodeModel.MtrSkillLevelCode(**payload.dict())

def delete_skill_level_code_cruds(db:Session,get_id:int):
    return db.query(SkillLevelCodeModel.MtrSkillLevelCode).filter(SkillLevelCodeModel.MtrSkillLevelCode.skill_level_code_id==get_id).delete(synchronize_session=False)
    
def put_skill_level_code_cruds(db:Session,payload:SkillLevelCodeModel.MtrSkillLevelCode, get_id:int):
    edit_skill_level_code = db.query(SkillLevelCodeModel.MtrSkillLevelCode).filter(SkillLevelCodeModel.MtrSkillLevelCode.skill_level_code_id==get_id)
    edit_skill_level_code.update(payload.dict())
    messages_skill_level_code = edit_skill_level_code.first()
    return edit_skill_level_code, messages_skill_level_code

def patch_skill_level_code_cruds(db:Session, get_id:int):
    return db.query(SkillLevelCodeModel.MtrSkillLevelCode).filter(SkillLevelCodeModel.MtrSkillLevelCode.skill_level_code_id==get_id).first()

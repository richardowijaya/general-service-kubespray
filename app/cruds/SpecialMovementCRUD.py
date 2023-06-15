from sqlalchemy.orm import Session
from models import SpecialMovementModel

def get_special_movements_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(SpecialMovementModel.MtrSpecialMovement).order_by(SpecialMovementModel.MtrSpecialMovement.special_movement_id).offset(offset).limit(limit).all()


def get_special_movement_cruds(db:Session,get_id:int):
    return  db.query(SpecialMovementModel.MtrSpecialMovement).filter(SpecialMovementModel.MtrSpecialMovement.special_movement_id==get_id).first()
    

def post_special_movement_cruds(db:Session, payload:SpecialMovementModel.MtrSpecialMovement):
    return SpecialMovementModel.MtrSpecialMovement(**payload.dict())

def delete_special_movement_cruds(db:Session,get_id:int):
    return db.query(SpecialMovementModel.MtrSpecialMovement).filter(SpecialMovementModel.MtrSpecialMovement.special_movement_id==get_id).delete(synchronize_session=False)
    
def put_special_movement_cruds(db:Session,payload:SpecialMovementModel.MtrSpecialMovement, get_id:int):
    edit_special_movement = db.query(SpecialMovementModel.MtrSpecialMovement).filter(SpecialMovementModel.MtrSpecialMovement.special_movement_id==get_id)
    edit_special_movement.update(payload.dict())
    messages_special_movement = edit_special_movement.first()
    return edit_special_movement, messages_special_movement

def patch_special_movement_cruds(db:Session, get_id:int):
    return db.query(SpecialMovementModel.MtrSpecialMovement).filter(SpecialMovementModel.MtrSpecialMovement.special_movement_id==get_id).first()

from sqlalchemy.orm import Session
from models import WorkOrderTypeModel

def get_work_order_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(WorkOrderTypeModel.MtrWorkorderType).order_by(WorkOrderTypeModel.MtrWorkorderType.work_order_type_id).offset(offset).limit(limit).all()


def get_work_order_type_cruds(db:Session,get_id:int):
    return  db.query(WorkOrderTypeModel.MtrWorkorderType).filter(WorkOrderTypeModel.MtrWorkorderType.work_order_type_id==get_id).first()
    

def post_work_order_type_cruds(db:Session, payload:WorkOrderTypeModel.MtrWorkorderType):
    return WorkOrderTypeModel.MtrWorkorderType(**payload.dict())

def delete_work_order_type_cruds(db:Session,get_id:int):
    return db.query(WorkOrderTypeModel.MtrWorkorderType).filter(WorkOrderTypeModel.MtrWorkorderType.work_order_type_id==get_id).delete(synchronize_session=False)
    
def put_work_order_type_cruds(db:Session,payload:WorkOrderTypeModel.MtrWorkorderType, get_id:int):
    edit_work_order_type = db.query(WorkOrderTypeModel.MtrWorkorderType).filter(WorkOrderTypeModel.MtrWorkorderType.work_order_type_id==get_id)
    edit_work_order_type.update(payload.dict())
    messages_work_order_type = edit_work_order_type.first()
    return edit_work_order_type, messages_work_order_type

def patch_work_order_type_cruds(db:Session, get_id:int):
    return db.query(WorkOrderTypeModel.MtrWorkorderType).filter(WorkOrderTypeModel.MtrWorkorderType.work_order_type_id==get_id).first()

from sqlalchemy.orm import Session
from models import WorkOrderTransactionTypeModel

def get_work_order_transaction_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(WorkOrderTransactionTypeModel.MtrWorkOrderTransactionType).order_by(WorkOrderTransactionTypeModel.MtrWorkOrderTransactionType.work_order_transaction_type_id).offset(offset).limit(limit).all()


def get_work_order_transaction_type_cruds(db:Session,get_id:int):
    return  db.query(WorkOrderTransactionTypeModel.MtrWorkOrderTransactionType).filter(WorkOrderTransactionTypeModel.MtrWorkOrderTransactionType.work_order_transaction_type_id==get_id).first()
    

def post_work_order_transaction_type_cruds(db:Session, payload:WorkOrderTransactionTypeModel.MtrWorkOrderTransactionType):
    return WorkOrderTransactionTypeModel.MtrWorkOrderTransactionType(**payload.dict())

def delete_work_order_transaction_type_cruds(db:Session,get_id:int):
    return db.query(WorkOrderTransactionTypeModel.MtrWorkOrderTransactionType).filter(WorkOrderTransactionTypeModel.MtrWorkOrderTransactionType.work_order_transaction_type_id==get_id).delete(synchronize_session=False)
    
def put_work_order_transaction_type_cruds(db:Session,payload:WorkOrderTransactionTypeModel.MtrWorkOrderTransactionType, get_id:int):
    edit_work_order_transaction_type = db.query(WorkOrderTransactionTypeModel.MtrWorkOrderTransactionType).filter(WorkOrderTransactionTypeModel.MtrWorkOrderTransactionType.work_order_transaction_type_id==get_id)
    edit_work_order_transaction_type.update(payload.dict())
    messages_work_order_transaction_type = edit_work_order_transaction_type.first()
    return edit_work_order_transaction_type, messages_work_order_transaction_type

def patch_work_order_transaction_type_cruds(db:Session, get_id:int):
    return db.query(WorkOrderTransactionTypeModel.MtrWorkOrderTransactionType).filter(WorkOrderTransactionTypeModel.MtrWorkOrderTransactionType.work_order_transaction_type_id==get_id).first()

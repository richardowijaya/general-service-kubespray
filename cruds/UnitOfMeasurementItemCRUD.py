from sqlalchemy.orm import Session
from models import UnitOfMeasurementItemModel

def get_unit_of_measurement_items_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(UnitOfMeasurementItemModel.MtrUnitOfMeasurementItem).order_by(UnitOfMeasurementItemModel.MtrUnitOfMeasurementItem.unit_of_measurement_item_id).offset(offset).limit(limit).all()


def get_unit_of_measurement_item_cruds(db:Session,get_id:int):
    return  db.query(UnitOfMeasurementItemModel.MtrUnitOfMeasurementItem).filter(UnitOfMeasurementItemModel.MtrUnitOfMeasurementItem.unit_of_measurement_item_id==get_id).first()
    

def post_unit_of_measurement_item_cruds(db:Session, payload:UnitOfMeasurementItemModel.MtrUnitOfMeasurementItem):
    return UnitOfMeasurementItemModel.MtrUnitOfMeasurementItem(**payload.dict())

def delete_unit_of_measurement_item_cruds(db:Session,get_id:int):
    return db.query(UnitOfMeasurementItemModel.MtrUnitOfMeasurementItem).filter(UnitOfMeasurementItemModel.MtrUnitOfMeasurementItem.unit_of_measurement_item_id==get_id).delete(synchronize_session=False)
    
def put_unit_of_measurement_item_cruds(db:Session,payload:UnitOfMeasurementItemModel.MtrUnitOfMeasurementItem, get_id:int):
    edit_unit_of_measurement_item = db.query(UnitOfMeasurementItemModel.MtrUnitOfMeasurementItem).filter(UnitOfMeasurementItemModel.MtrUnitOfMeasurementItem.unit_of_measurement_item_id==get_id)
    edit_unit_of_measurement_item.update(payload.dict())
    messages_unit_of_measurement_item = edit_unit_of_measurement_item.first()
    return edit_unit_of_measurement_item, messages_unit_of_measurement_item

def patch_unit_of_measurement_item_cruds(db:Session, get_id:int):
    return db.query(UnitOfMeasurementItemModel.MtrUnitOfMeasurementItem).filter(UnitOfMeasurementItemModel.MtrUnitOfMeasurementItem.unit_of_measurement_item_id==get_id).first()

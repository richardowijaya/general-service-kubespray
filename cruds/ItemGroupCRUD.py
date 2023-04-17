from sqlalchemy.orm import Session
from models import ItemGroupModel

def get_item_groups_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(ItemGroupModel.MtrItemGroup).order_by(ItemGroupModel.MtrItemGroup.item_group_id).offset(offset).limit(limit).all()


def get_item_group_cruds(db:Session,get_id:int):
    return  db.query(ItemGroupModel.MtrItemGroup).filter(ItemGroupModel.MtrItemGroup.item_group_id==get_id).first()
    

def post_item_group_cruds(db:Session, payload:ItemGroupModel.MtrItemGroup):
    return ItemGroupModel.MtrItemGroup(**payload.dict())

def delete_item_group_cruds(db:Session,get_id:int):
    return db.query(ItemGroupModel.MtrItemGroup).filter(ItemGroupModel.MtrItemGroup.item_group_id==get_id).delete(synchronize_session=False)
    
def put_item_group_cruds(db:Session,payload:ItemGroupModel.MtrItemGroup, get_id:int):
    edit_item_group = db.query(ItemGroupModel.MtrItemGroup).filter(ItemGroupModel.MtrItemGroup.item_group_id==get_id)
    edit_item_group.update(payload.dict())
    messages_item_group = edit_item_group.first()
    return edit_item_group, messages_item_group

def patch_item_group_cruds(db:Session, get_id:int):
    return db.query(ItemGroupModel.MtrItemGroup).filter(ItemGroupModel.MtrItemGroup.item_group_id==get_id).first()

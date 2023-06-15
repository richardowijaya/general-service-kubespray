from sqlalchemy.orm import Session
from models import AfterSalesAreaModel

def get_after_sales_areas_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(AfterSalesAreaModel.MtrAfterSalesArea).order_by(AfterSalesAreaModel.MtrAfterSalesArea.after_sales_area_id).offset(offset).limit(limit).all()


def get_after_sales_area_cruds(db:Session,get_id:int):
    return  db.query(AfterSalesAreaModel.MtrAfterSalesArea).filter(AfterSalesAreaModel.MtrAfterSalesArea.after_sales_area_id==get_id).first()
    

def post_after_sales_area_cruds(db:Session, payload:AfterSalesAreaModel.MtrAfterSalesArea):
    return AfterSalesAreaModel.MtrAfterSalesArea(**payload.dict())

def delete_after_sales_area_cruds(db:Session,get_id:int):
    return db.query(AfterSalesAreaModel.MtrAfterSalesArea).filter(AfterSalesAreaModel.MtrAfterSalesArea.after_sales_area_id==get_id).delete(synchronize_session=False)
    
def put_after_sales_area_cruds(db:Session,payload:AfterSalesAreaModel.MtrAfterSalesArea, get_id:int):
    edit_after_sales_area = db.query(AfterSalesAreaModel.MtrAfterSalesArea).filter(AfterSalesAreaModel.MtrAfterSalesArea.after_sales_area_id==get_id)
    edit_after_sales_area.update(payload.dict())
    messages_after_sales_area = edit_after_sales_area.first()
    return edit_after_sales_area, messages_after_sales_area

def patch_after_sales_area_cruds(db:Session, get_id:int):
    return db.query(AfterSalesAreaModel.MtrAfterSalesArea).filter(AfterSalesAreaModel.MtrAfterSalesArea.after_sales_area_id==get_id).first()

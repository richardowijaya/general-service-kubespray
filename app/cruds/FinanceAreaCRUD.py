from sqlalchemy.orm import Session
from models import FinanceAreaModel

def get_finance_areas_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(FinanceAreaModel.MtrFinanceArea).order_by(FinanceAreaModel.MtrFinanceArea.finance_area_id).offset(offset).limit(limit).all()


def get_finance_area_cruds(db:Session,get_id:int):
    return  db.query(FinanceAreaModel.MtrFinanceArea).filter(FinanceAreaModel.MtrFinanceArea.finance_area_id==get_id).first()
    

def post_finance_area_cruds(db:Session, payload:FinanceAreaModel.MtrFinanceArea):
    return FinanceAreaModel.MtrFinanceArea(**payload.dict())

def delete_finance_area_cruds(db:Session,get_id:int):
    return db.query(FinanceAreaModel.MtrFinanceArea).filter(FinanceAreaModel.MtrFinanceArea.finance_area_id==get_id).delete(synchronize_session=False)
    
def put_finance_area_cruds(db:Session,payload:FinanceAreaModel.MtrFinanceArea, get_id:int):
    edit_finance_area = db.query(FinanceAreaModel.MtrFinanceArea).filter(FinanceAreaModel.MtrFinanceArea.finance_area_id==get_id)
    edit_finance_area.update(payload.dict())
    messages_finance_area = edit_finance_area.first()
    return edit_finance_area, messages_finance_area

def patch_finance_area_cruds(db:Session, get_id:int):
    return db.query(FinanceAreaModel.MtrFinanceArea).filter(FinanceAreaModel.MtrFinanceArea.finance_area_id==get_id).first()

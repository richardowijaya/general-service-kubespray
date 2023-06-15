from sqlalchemy.orm import Session
from models import PriceListCodeModel

def get_price_list_codes_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(PriceListCodeModel.MtrPriceListCode).order_by(PriceListCodeModel.MtrPriceListCode.price_list_code_id).offset(offset).limit(limit).all()


def get_price_list_code_cruds(db:Session,get_id:int):
    return  db.query(PriceListCodeModel.MtrPriceListCode).filter(PriceListCodeModel.MtrPriceListCode.price_list_code_id==get_id).first()
    

def post_price_list_code_cruds(db:Session, payload:PriceListCodeModel.MtrPriceListCode):
    return PriceListCodeModel.MtrPriceListCode(**payload.dict())

def delete_price_list_code_cruds(db:Session,get_id:int):
    return db.query(PriceListCodeModel.MtrPriceListCode).filter(PriceListCodeModel.MtrPriceListCode.price_list_code_id==get_id).delete(synchronize_session=False)
    
def put_price_list_code_cruds(db:Session,payload:PriceListCodeModel.MtrPriceListCode, get_id:int):
    edit_price_list_code = db.query(PriceListCodeModel.MtrPriceListCode).filter(PriceListCodeModel.MtrPriceListCode.price_list_code_id==get_id)
    edit_price_list_code.update(payload.dict())
    messages_price_list_code = edit_price_list_code.first()
    return edit_price_list_code, messages_price_list_code

def patch_price_list_code_cruds(db:Session, get_id:int):
    return db.query(PriceListCodeModel.MtrPriceListCode).filter(PriceListCodeModel.MtrPriceListCode.price_list_code_id==get_id).first()

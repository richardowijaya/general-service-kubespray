from sqlalchemy.orm import Session
from models import TaxFormatTypeModel

def get_tax_format_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(TaxFormatTypeModel.MtrTaxFormatType).order_by(TaxFormatTypeModel.MtrTaxFormatType.tax_format_type_id).offset(offset).limit(limit).all()


def get_tax_format_type_cruds(db:Session,get_id:int):
    return  db.query(TaxFormatTypeModel.MtrTaxFormatType).filter(TaxFormatTypeModel.MtrTaxFormatType.tax_format_type_id==get_id).first()
    

def post_tax_format_type_cruds(db:Session, payload:TaxFormatTypeModel.MtrTaxFormatType):
    return TaxFormatTypeModel.MtrTaxFormatType(**payload.dict())

def delete_tax_format_type_cruds(db:Session,get_id:int):
    return db.query(TaxFormatTypeModel.MtrTaxFormatType).filter(TaxFormatTypeModel.MtrTaxFormatType.tax_format_type_id==get_id).delete(synchronize_session=False)
    
def put_tax_format_type_cruds(db:Session,payload:TaxFormatTypeModel.MtrTaxFormatType, get_id:int):
    edit_tax_format_type = db.query(TaxFormatTypeModel.MtrTaxFormatType).filter(TaxFormatTypeModel.MtrTaxFormatType.tax_format_type_id==get_id)
    edit_tax_format_type.update(payload.dict())
    messages_tax_format_type = edit_tax_format_type.first()
    return edit_tax_format_type, messages_tax_format_type

def patch_tax_format_type_cruds(db:Session, get_id:int):
    return db.query(TaxFormatTypeModel.MtrTaxFormatType).filter(TaxFormatTypeModel.MtrTaxFormatType.tax_format_type_id==get_id).first()

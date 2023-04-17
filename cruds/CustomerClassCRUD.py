from sqlalchemy.orm import Session
from models import CustomerClassModel

def get_customer_classes_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(CustomerClassModel.MtrCustomerClass).order_by(CustomerClassModel.MtrCustomerClass.customer_class_id).offset(offset).limit(limit).all()


def get_customer_class_cruds(db:Session,get_id:int):
    return  db.query(CustomerClassModel.MtrCustomerClass).filter(CustomerClassModel.MtrCustomerClass.customer_class_id==get_id).first()
    

def post_customer_class_cruds(db:Session, payload:CustomerClassModel.MtrCustomerClass):
    return CustomerClassModel.MtrCustomerClass(**payload.dict())

def delete_customer_class_cruds(db:Session,get_id:int):
    return db.query(CustomerClassModel.MtrCustomerClass).filter(CustomerClassModel.MtrCustomerClass.customer_class_id==get_id).delete(synchronize_session=False)
    
def put_customer_class_cruds(db:Session,payload:CustomerClassModel.MtrCustomerClass, get_id:int):
    edit_customer_class = db.query(CustomerClassModel.MtrCustomerClass).filter(CustomerClassModel.MtrCustomerClass.customer_class_id==get_id)
    edit_customer_class.update(payload.dict())
    messages_customer_class = edit_customer_class.first()
    return edit_customer_class, messages_customer_class

def patch_customer_class_cruds(db:Session, get_id:int):
    return db.query(CustomerClassModel.MtrCustomerClass).filter(CustomerClassModel.MtrCustomerClass.customer_class_id==get_id).first()

from sqlalchemy.orm import Session
from models import CustomerTypeFlagListModel

def get_customer_type_flag_lists_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(CustomerTypeFlagListModel.MtrCustomerTypeFlagList).order_by(CustomerTypeFlagListModel.MtrCustomerTypeFlagList.customer_type_flag_list_id).offset(offset).limit(limit).all()


def get_customer_type_flag_list_cruds(db:Session,get_id:int):
    return  db.query(CustomerTypeFlagListModel.MtrCustomerTypeFlagList).filter(CustomerTypeFlagListModel.MtrCustomerTypeFlagList.customer_type_flag_list_id==get_id).first()
    

def post_customer_type_flag_list_cruds(db:Session, payload:CustomerTypeFlagListModel.MtrCustomerTypeFlagList):
    return CustomerTypeFlagListModel.MtrCustomerTypeFlagList(**payload.dict())

def delete_customer_type_flag_list_cruds(db:Session,get_id:int):
    return db.query(CustomerTypeFlagListModel.MtrCustomerTypeFlagList).filter(CustomerTypeFlagListModel.MtrCustomerTypeFlagList.customer_type_flag_list_id==get_id).delete(synchronize_session=False)
    
def put_customer_type_flag_list_cruds(db:Session,payload:CustomerTypeFlagListModel.MtrCustomerTypeFlagList, get_id:int):
    edit_customer_type_flag_list = db.query(CustomerTypeFlagListModel.MtrCustomerTypeFlagList).filter(CustomerTypeFlagListModel.MtrCustomerTypeFlagList.customer_type_flag_list_id==get_id)
    edit_customer_type_flag_list.update(payload.dict())
    messages_customer_type_flag_list = edit_customer_type_flag_list.first()
    return edit_customer_type_flag_list, messages_customer_type_flag_list

def patch_customer_type_flag_list_cruds(db:Session, get_id:int):
    return db.query(CustomerTypeFlagListModel.MtrCustomerTypeFlagList).filter(CustomerTypeFlagListModel.MtrCustomerTypeFlagList.customer_type_flag_list_id==get_id).first()

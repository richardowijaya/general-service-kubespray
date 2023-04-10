from fastapi import APIRouter,Depends,HTTPException,status,Response
from cruds import CountryCRUD
from models import CountryModel
from schemas import CountrySchema
from sqlalchemy.orm import Session
from configs.database import get_db

router = APIRouter(tags=["Country"],prefix="/api/general")

@router.get("/Country")
def get_countries(db:Session=Depends(get_db)):
    items = CountryCRUD.get_countries_cruds(db)
    if not items:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="data not found")
    return {
        "status" : "success",
        "results" : len(items),
        "data" : items
    }

@router.get("/Country/{id}")
def get_country(id:int,db:Session=Depends(get_db)):
    item = CountryCRUD.get_country_id(db,id)
    if not item:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="data id:{id} not found")
    return {
        "status" : "success",
        "data" : item
    }

@router.post("/Country")
def post_country(payload:CountrySchema.MtrCountrySchema,db:Session=Depends(get_db)):
    new_data = CountryModel.MtrCountry(**payload.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {
        "status" : "success",
        "new country" : new_data
    }

@router.delete("/Country/{id}")
def delete_country(id:int,db:Session=Depends(get_db)):
    del_data = CountryCRUD.delete_country_crud(id,db)
    if not del_data:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="data id:{id} not found")
    db.delete(del_data)
    db.commit()
    return Response(status_code=status.HTTP_200_OK)

@router.put("/Country/{id}")
def update_country(id:int,payload:CountrySchema.MtrCountrySchema,db:Session=Depends(get_db)):
    check_id = db.query(CountryModel.MtrCountry).filter(CountryModel.MtrCountry.country_id==id)
    update_data_new = check_id.first()
    #check_id = CountryCRUD.update_country_cruds(payload,db,)
    #update_data_new = check_id.first()
    if not check_id:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="data id:{id} not found")
    update_data = payload.dict(exclude_unset=True)
    check_id.filter(CountryModel.MtrCountry.country_id==id).update(update_data,synchronize_session=False)
    db.commit()
    db.refresh(update_data_new)
    return{
        "status" : "updated",
        "data" : update_data_new
    }
    
from fastapi import APIRouter,Depends,HTTPException,status
from cruds import CountryCRUD
from models import CountryModel
from schemas import CountrySchema
from sqlalchemy.orm import Session
from configs.database import get_db

router = APIRouter(tags=["Province"],prefix="/api/general")

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
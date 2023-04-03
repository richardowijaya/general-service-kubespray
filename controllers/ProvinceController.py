from fastapi import APIRouter,Depends,HTTPException,status
from cruds import ProvinceCRUD
from models import ProvinceModel
from schemas import ProvinceSchema
from sqlalchemy.orm import Session
from database.database import get_db
from repositories.AddRoute import add_route

router = APIRouter(tags=["Country"],prefix="/api/general")

@router.get("/Province")
def get_provinces(db:Session=Depends(get_db)):
    items = ProvinceCRUD.get_provinces_cruds(db)
    if not items:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="data not found")
    return {
        "status" : "success",
        "results" : len(items),
        "data" : items
    }

@router.post("/Province")
def post_province(payload:ProvinceSchema.MtrProvinceSchema,db:Session=Depends(get_db)):
    new_data = ProvinceModel.MtrProvince(**payload.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return {
        "status" : "success",
        "new province" : new_data
    }

add_route(router)
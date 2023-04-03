from fastapi import APIRouter,Depends,HTTPException,status
from cruds import RegionCRUD
from models import RegionModel
from schemas import RegionSchema
from sqlalchemy.orm import Session
from database.database import get_db
from repositories.AddRoute import add_route

router = APIRouter(tags=["Region"],prefix="/api/general")
@router.get("/Region")
def get_regions(db:Session=Depends(get_db)):
    items = RegionCRUD.get_regioncruds(db)
    if not items:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="data not found")
    return{
        "status" : "success",
        "results" : len(items),
        "data" : items
    }

@router.post("/Region")
def post_new_region(payload:RegionSchema.MtrRegionSchema,db:Session=Depends(get_db)):
    new_data = RegionModel.MtrRegion(**payload.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {
        "status" : "success",
        "new Preprinted Region" : new_data
    }

add_route(router)
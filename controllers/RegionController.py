from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from configs.database import get_db
from cruds import RegionCRUD
from schemas import RegionSchema

router = APIRouter(tags=["Region"],prefix="/api/general")

@router.get("/region",status_code=status.HTTP_200_OK)
async def get_all_data(db:Session=Depends(get_db)):
    results = RegionCRUD.get_region_all(db,0,5)
    if not results:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    return RegionSchema.MtrRegionResponses(status_code=200,msg_status="success",data=results)

@router.get("/region/{id}",status_code=status.HTTP_200_OK)
async def get_by_id(id:int,db:Session=Depends(get_db)):
    result = RegionCRUD.get_region_by_id(db,id)
    if not result:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"data with ID {id} not existed")
    return RegionSchema.MtrRegionResponse(status_code=200,msg_status="success",data=result)

@router.delete("/region/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_data(id:int,db:Session=Depends(get_db)):
    check = RegionCRUD.del_region(db,id)
    if not check:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data with ID {id} is invalid")
    return check

@router.post("/region",status_code=status.HTTP_201_CREATED)
async def create_data(request:RegionSchema.MtrRegionRequest,db:Session=Depends(get_db)):
    new_data = RegionCRUD.post_new_region(db,request)
    if not new_data:
        return HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"data already existed")
    return RegionSchema.MtrRegionResponse(status_code=200,msg_status="success",data=new_data)

@router.put("/region/{id}",status_code=status.HTTP_200_OK)
async def update_data(request:RegionSchema.MtrRegionRequest,id:int,db:Session=Depends(get_db)):
    update_data = RegionCRUD.update_region(db,id,request)
    return RegionSchema.MtrRegionResponse(status_code=200,msg_status="success",data=update_data)
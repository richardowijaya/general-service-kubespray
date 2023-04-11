from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from configs.database import get_db
from cruds import AreaCRUD
from schemas import AreaSchema

router = APIRouter(tags=["Area"],prefix="/api/general")

@router.get("/area",status_code=status.HTTP_200_OK)
async def get_all_data(db:Session=Depends(get_db)):
    results = AreaCRUD.get_area_all(db,0,5)
    if not results:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    return AreaSchema.MtrAreaResponses(status_code=200,msg_status="success",data=results)

@router.get("/area/{id}",status_code=status.HTTP_200_OK)
async def get_by_id(id:int,db:Session=Depends(get_db)):
    result = AreaCRUD.get_area_by_id(db,id)
    if not result:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"data with ID {id} not existed")
    return AreaSchema.MtrAreaResponse(status_code=200,msg_status="success",data=result)

@router.delete("/area/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_data(id:int,db:Session=Depends(get_db)):
    check = AreaCRUD.del_area(db,id)
    if not check:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data with ID {id} is invalid")
    return check

@router.post("/area",status_code=status.HTTP_201_CREATED)
async def create_data(request:AreaSchema.MtrAreaRequest,db:Session=Depends(get_db)):
    new_data = AreaCRUD.post_new_area(db,request)
    if not new_data:
        return HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"data already existed")
    return AreaSchema.MtrAreaResponse(status_code=200,msg_status="success",data=new_data)

@router.put("/area/{id}",status_code=status.HTTP_200_OK)
async def update_data(request:AreaSchema.MtrAreaRequest,id:int,db:Session=Depends(get_db)):
    update_data = AreaCRUD.update_area(db,id,request)
    return AreaSchema.MtrAreaResponse(status_code=200,msg_status="success",data=update_data)
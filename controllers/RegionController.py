<<<<<<< HEAD
from fastapi import APIRouter,Depends,HTTPException,status,Query
=======
from fastapi import APIRouter,Depends,HTTPException,status
>>>>>>> 6c332901c44706e2cd630677bcf753c81a5cd6b3
from sqlalchemy.orm import Session
from configs.database import get_db
from cruds import RegionCRUD
from schemas import RegionSchema
<<<<<<< HEAD
from payloads import Pagination
from typing import Optional
=======
>>>>>>> 6c332901c44706e2cd630677bcf753c81a5cd6b3

router = APIRouter(tags=["Region"],prefix="/api/general")

@router.get("/region",status_code=status.HTTP_200_OK)
<<<<<<< HEAD
async def get_all_data(query_params:list[str]|None = Query(None),page:Optional[int]=None,page_limit:Optional[int]=None,db:Session=Depends(get_db)):
    page,limit,total_rows,total_pages,results = RegionCRUD.get_region_all(db,page,page_limit)
    if not results:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    return Pagination.PaginationSchema(status="OK",msg_status="success",page_limit=limit,page=page,total_rows=total_rows,total_pages=total_pages,rows=results)
=======
async def get_all_data(db:Session=Depends(get_db)):
    results = RegionCRUD.get_region_all(db,0,5)
    if not results:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    return RegionSchema.MtrRegionResponses(status_code=200,msg_status="success",data=results)
>>>>>>> 6c332901c44706e2cd630677bcf753c81a5cd6b3

@router.get("/region/{id}",status_code=status.HTTP_200_OK)
async def get_by_id(id:int,db:Session=Depends(get_db)):
    result = RegionCRUD.get_region_by_id(db,id)
    if not result:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"data with ID {id} not existed")
    return RegionSchema.MtrRegionResponse(status_code=200,msg_status="success",data=result)

<<<<<<< HEAD
@router.get("/region_params")
async def get_by_params(param:str,db:Session=Depends(get_db)):
    results = RegionCRUD.get_region_by_params(db,param)
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    return RegionSchema.MtrRegionResponses(status_code=200,msg_status="success",data=results)
    
=======
>>>>>>> 6c332901c44706e2cd630677bcf753c81a5cd6b3
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
<<<<<<< HEAD
    return RegionSchema.MtrRegionResponse(status_code=200,msg_status="success",data=update_data)

@router.get("/region/test", status_code=status.HTTP_200_OK)
async def get_all_data(session: Session = Depends(get_db)):
    
    results = RegionCRUD.get_all_users(session)

    return results
=======
    return RegionSchema.MtrRegionResponse(status_code=200,msg_status="success",data=update_data)
>>>>>>> 6c332901c44706e2cd630677bcf753c81a5cd6b3

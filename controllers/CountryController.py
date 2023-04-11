from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from configs.database import get_db
from cruds import CountryCRUD
from schemas import CountrySchema

router = APIRouter(tags=["Country"],prefix="/api/general")

@router.get("/country",status_code=status.HTTP_200_OK)
async def get_all_data(db:Session=Depends(get_db)):
    results = CountryCRUD.get_country_all(db,0,100)
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    return CountrySchema.MtrCountryResponses(status_code=200,msg_status="success",data=results)

@router.get("/country/{id}",status_code=status.HTTP_200_OK)
async def get_by_id(id:int,db:Session=Depends(get_db)):
    result = CountryCRUD.get_country_by_id(db,id)
    print(result,type(result))
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data with ID {id} not existed")
    return CountrySchema.MtrCountryResponse(status_code=200,msg_status="success",data=result)

@router.delete("/country/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_data(id:int,db:Session=Depends(get_db)):
    check = CountryCRUD.del_country(db,id)
    print(check)
    if not check:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data with ID {id} is invalid")
    return check

@router.post("/country",status_code=status.HTTP_201_CREATED)
async def create_data(request:CountrySchema.MtrCountryRequest,db:Session=Depends(get_db)):
    new_data = CountryCRUD.post_new_country(db,request)
    if not new_data:
        return HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"data already existed")
    return CountrySchema.MtrCountryResponse(status_code=200,msg_status="success",data=new_data)

@router.put("/country/{id}",status_code=status.HTTP_200_OK)
async def update_data(request:CountrySchema.MtrCountryRequest,id:int,db:Session=Depends(get_db)):
    update_data = CountryCRUD.update_country(db,id,request)
    return CountrySchema.MtrCountryResponse(status_code=200,msg_status="success",data=update_data)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import engine
from models import RegionModel
from controllers import RegionController

RegionModel.Base.metadata.create_all(bind=engine)

app = FastAPI()

# utilized for incoming request from Front End / API Gateway
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(RegionController.router,tags=["DMS_General_Master"],prefix="/api/general")
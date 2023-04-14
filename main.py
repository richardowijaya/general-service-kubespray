from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import utils.AddControllers #manual function that created using basic libraries in python
from utils.AddModelsEngine import addmodels #manual function that created models and base engine


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


addmodels()

app.include_router(utils.AddControllers.populate_router)
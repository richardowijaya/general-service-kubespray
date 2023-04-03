from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import repositories.AddControllers #manual function that created using basic libraries in python
#from repositories.AddRoute import router

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

#app.include_router(router)
app.include_router(repositories.AddControllers.populate_router)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import utils.AddControllers #manual function that created using basic libraries in python
from utils.AddModelsEngine import addmodels #manual function that created models and base engine
from logging_lib import RouterLoggingMiddleware
import logging.config
import logging
import sys

logging_config = {
    "version": 1,
    "formatters": {
        "json": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(process)s %(levelname)s %(name)s %(module)s %(funcName)s %(lineno)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "json",
            "stream": sys.stderr,
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "app.log",
            "formatter": "json",
            "maxBytes": 1000000000,
            "backupCount":1,
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console",
            "file",
        ],
        "propagate": True
    }
}

logging.config.dictConfig(logging_config)

app = FastAPI()

# utilized for incoming request from Front End / API Gateway
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    RouterLoggingMiddleware
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

addmodels()

app.include_router(utils.AddControllers.populate_router)
import os
import importlib
from fastapi import APIRouter

populate_router = APIRouter()

path = os.getcwd()
prev_path = path + "//controllers"
router = os.listdir(prev_path)
for ch in router:
    if ch != '__pycache__':
        get_controller = ch.replace(".py","")
        from_module = importlib.import_module("controllers." + get_controller)
        populate_router.include_router(from_module.router)  
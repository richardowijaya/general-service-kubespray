import os
import importlib
from fastapi import APIRouter

populate_router = APIRouter()

path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
prev_path = path + "\\src\\" + "\\controllers"
router = os.listdir(prev_path)
controller = []
for ch in range (len(router)-1):
    get_controller = router[ch].replace(".py","")
    from_module = importlib.import_module("controllers." + get_controller)
    populate_router.include_router(from_module.router)
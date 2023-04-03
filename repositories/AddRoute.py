from fastapi import APIRouter

router = APIRouter()

def add_route(current:APIRouter):
    router.include_router(current)